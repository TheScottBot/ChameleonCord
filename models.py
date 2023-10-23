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

__all__ = ("CategoryCard",
           "CategoryDeck",
           "PlayerDeck",
           "PlayerCard",
           "Player",
           "Game",)


class CategoryCard(object):
    def __init__(self, title, categories):
        self.__title = title
        self.__categories: dict = categories

    @property
    def title(self):
        return self.__title

    @property
    def categories(self):
        return self.__categories

    def categories_formatted(self):
        return_value = f'# {self.__title}\n\n```| A1: {self.categories["A1"]} || A2 : {self.categories["A2"]} || A3: {self.categories["A3"]} || A4: {self.categories["A4"]} |\n' + f'| B1: {self.categories["B1"]} || B2 : {self.categories["B2"]} || B3: {self.categories["B3"]} || B4: {self.categories["B4"]} |\n' + f'| C1: {self.categories["C1"]} || C2 : {self.categories["C2"]} || C3: {self.categories["C3"]} || C4: {self.categories["C4"]} |\n' + f'| D1: {self.categories["D1"]} || D2 : {self.categories["D2"]} || D3: {self.categories["D3"]} || D4: {self.categories["D4"]} |```\n'
        return return_value


class CategoryDeck(object):
    def __init__(self, cards):
        self.__cards: list[CategoryCard] = cards

    @property
    def cards(self):
        return self.__cards


class PlayerCard(object):
    def __init__(self, colour, grid):
        self.__colour = colour
        self.__grid: dict = grid

    @property
    def colour(self):
        return self.__colour

    @property
    def grid(self):
        return self.__grid


class PlayerDeck(object):
    __slots__ = "__cards"

    def __init__(self, cards):
        self.__cards: list[PlayerCard] = cards

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        self.__cards = value

    def grid_formatted(self, colour: str):
        if colour == "green":
            grid = self.cards[0].grid
        elif colour == "blue":
            grid = self.cards[1].grid
        else:
            # fuck it, just default to green
            grid = self.cards[0].grid

        return_value = f'```    | One || Two || Three || Four || Five || Six |\n| 1 | {grid["One.1"]}  || {grid["Two.1"]}  || {grid["Three.1"]}    || {grid["Four.1"]}   || {grid["Five.1"]}   || {grid["Six.1"]}  |\n| 2 | {grid["One.2"]}  || {grid["Two.2"]}  || {grid["Three.2"]}    || {grid["Four.2"]}   || {grid["Five.2"]}   || {grid["Six.2"]}  |\n| 3 | {grid["One.3"]}  || {grid["Two.3"]}  || {grid["Three.3"]}    || {grid["Four.3"]}   || {grid["Five.3"]}   || {grid["Six.3"]}  |\n| 4 | {grid["One.4"]}  || {grid["Two.4"]}  || {grid["Three.4"]}    || {grid["Four.4"]}   || {grid["Five.4"]}   || {grid["Six.4"]}  |\n| 5 | {grid["One.5"]}  || {grid["Two.5"]}  || {grid["Three.5"]}    || {grid["Four.5"]}   || {grid["Five.5"]}   || {grid["Six.5"]}  |\n| 6 | {grid["One.6"]}  || {grid["Two.6"]}  || {grid["Three.6"]}    || {grid["Four.6"]}   || {grid["Five.6"]}   || {grid["Six.6"]}  |\n| 7 | {grid["One.7"]}  || {grid["Two.7"]}  || {grid["Three.7"]}    || {grid["Four.7"]}   || {grid["Five.7"]}   || {grid["Six.7"]}  |\n| 8 | {grid["One.8"]}  || {grid["Two.8"]}  || {grid["Three.8"]}    || {grid["Four.8"]}   || {grid["Five.8"]}   || {grid["Six.8"]}  |\n```'
        return return_value


class Player(object):
    __slots__ = ("__name", "__id", "__is_chameleon")

    def __init__(self, name, id):
        self.__name: str = name
        self.__id: str = id
        self.is_chameleon: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def is_chameleon(self):
        return self.__is_chameleon

    @is_chameleon.setter
    def is_chameleon(self, value):
        self.__is_chameleon = value


class Game(object):
    __slots__ = ("__players", "__player_deck", "__category_deck")

    def __init__(self, players: list[Player], player_deck: PlayerDeck, category_deck: CategoryDeck):
        self.__players: list[Player] = players
        self.__player_deck: PlayerDeck = player_deck
        self.__category_deck: CategoryDeck = category_deck

    @property
    def players(self):
        return self.__players

    def add_player(self, player: Player):
        self.__players.append(player)

    def clear_players(self):
        self.__players.clear()

    @property
    def player_deck(self):
        return self.__player_deck

    @player_deck.setter
    def player_deck(self, value):
        self.__player_deck = value

    @property
    def category_deck(self):
        return self.__category_deck

    @category_deck.setter
    def category_deck(self, value):
        self.__category_deck = value

    def assign_chameleon(self):
        value_to_chameleon = random.randint(0, self.__players.__len__()-1)
        self.__players[value_to_chameleon].is_chameleon = True
        print("Player " + str(value_to_chameleon+1) + " is the chameleon")