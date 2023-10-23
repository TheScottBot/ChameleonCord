import random

from discord.ext import commands
import category_deck
import player_deck
from models import Player, Game


class Example(commands.Cog):
    __slots__ = ("bot", "__game")

    def __init__(self, bot):
        self.bot = bot
        self.__game: Game = Game(players=[], player_deck=player_deck.DECK, category_deck=category_deck.DECK)

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command(name="cdraw")
    async def print(self, ctx, *args):
        card = random.choice(self.__game.category_deck.cards)
        print(len(self.__game.category_deck.cards))
        print(card.title)

        self.__game.category_deck.cards.remove(card)
        await ctx.channel.send(card.categories_formatted())

    @commands.command(name="register")
    async def register_player(self, ctx, *args):
        new_player = Player(name=ctx.author.display_name, id=ctx.author.id)
        if self.player_in_game(new_player.id):
            print("Player is already registered")
            return

        self.__game.players.append(new_player)
        await ctx.channel.send(f'Player "{new_player.name}" has been added to the game')

    @commands.command(name="pdraw")
    async def draw_player_cards(self, ctx, colour: str, *args):
        chameleon = random.choice(self.__game.players)
        # do this better as it sucks
        for i in range(len(self.__game.players)):
            if self.__game.players[i].id == chameleon.id:
                self.__game.players[i].is_chameleon = True
                discord_user = self.bot.get_user(chameleon.id)
                await discord_user.send("You are the chameleon")
            if not self.__game.players[i].is_chameleon:
                discord_user = self.bot.get_user(self.__game.players[i].id)
                await discord_user.send(self.__game.player_deck.grid_formatted(colour))
                self.test(colour=colour)

        # for i in range(len(self.__game.players)):


    @commands.command(name="next")
    async def next_round_setup(self, ctx, *args):
        for i in range(len(self.__game.players)):
            if self.__game.players[i].is_chameleon:
                await ctx.channel.send(f'{self.__game.players[i].name} was the chameleon')
            self.__game.players[i].is_chameleon = False

    def test(self, colour: str):
        return self.__game.player_deck.grid_formatted(colour=colour)

    def player_in_game(self, player_id: str) -> bool:
        if any(player.id == player_id for player in self.__game.players):
            return True
        return False





async def setup(bot):
    await bot.add_cog(Example(bot))