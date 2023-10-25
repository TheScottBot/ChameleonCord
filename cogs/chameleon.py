"""
The MIT License (MIT)

Copyright (c) 2023-present ChameleonCord

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import random

from discord.ext import commands
import category_deck
import player_deck
from models import Player, Game


class Example(commands.Cog):
    __slots__ = ("bot", "__game", "__current_colour", "__first_round")

    def __init__(self, bot):
        self.bot = bot
        self.__game: Game = Game(players=[], player_deck=player_deck.DECK, category_deck=category_deck.DECK)
        self.__current_colour = "green"
        self.__first_round = True

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command(name="register")
    async def register_player(self, ctx, *args):
        new_player = Player(name=ctx.author.display_name, id=ctx.author.id)
        if self.player_in_game(new_player.id):
            print("Player is already registered")
            return

        self.__game.players.append(new_player)
        await ctx.channel.send(f'Player "{new_player.name}" has been added to the game')

    async def draw_category_card(self, ctx):
        card = random.choice(self.__game.category_deck.cards)
        print(len(self.__game.category_deck.cards))
        print(card.title)

        self.__game.category_deck.cards.remove(card)
        await ctx.channel.send(card.categories_formatted())

    async def draw_player_cards(self, colour: str):
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

    @commands.command(name="next")
    async def next_round_setup(self, ctx, *args):
        if not self.__first_round:
            for i in range(len(self.__game.players)):
                if self.__game.players[i].is_chameleon:
                    await ctx.channel.send(f'{self.__game.players[i].name} was the chameleon')
                self.__game.players[i].is_chameleon = False
            self.__first_round = False
        self.assign_colour()
        await self.draw_player_cards(self.__current_colour)
        await self.draw_category_card(ctx)

    def player_in_game(self, player_id: str) -> bool:
        if any(player.id == player_id for player in self.__game.players):
            return True
        return False

    def assign_colour(self):
        if self.__current_colour == "green":
            self.__current_colour = "blue"
        else:
            self.__current_colour = "green"


async def setup(bot):
    await bot.add_cog(Example(bot))