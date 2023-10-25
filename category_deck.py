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

from models import CategoryCard, CategoryDeck

sports__star_dict = {
    "A1": "Tiger Woods",
    "A2": "Michael Phelps",
    "A3": "Bradley Wiggins",
    "A4": "Lewis Hamilton",
    "B1": "Tanni Grey-Thompson",
    "B2": "Johanna Konta",
    "B3": "Johnny Wilkinson",
    "B4": "Maria Sharapova",
    "C1": "Michael Jordan",
    "C2": "Muhammad Ali",
    "C3": "Paula Radcliffe",
    "C4": "Usain Bolt",
    "D1": "David Beckham",
    "D2": "Kelly Holmes",
    "D3": "Jess Ennis-Hill",
    "D4": "Laura Trott",
}

food_dict = {
    "A1": "Pizza",
    "A2": "Pasta",
    "A3": "Eggs",
    "A4": "Sausage",
    "B1": "Potatoes",
    "B2": "Salad",
    "B3": "Cheese",
    "B4": "Ice Cream",
    "C1": "Fish",
    "C2": "Soup",
    "C3": "Fruit",
    "C4": "Chocolate",
    "D1": "Cake",
    "D2": "Bread",
    "D3": "Chicken",
    "D4": "Beef",
}

wedding_anniversaries_dict = {
    "A1": "Wood",
    "A2": "Bronze",
    "A3": "Crystal",
    "A4": "Pearl",
    "B1": "China",
    "B2": "Gold",
    "B3": "Flowers",
    "B4": "Coral",
    "C1": "Paper",
    "C2": "Ruby",
    "C3": "Silk",
    "C4": "Tin",
    "D1": "Cotton",
    "D2": "Diamond",
    "D3": "Leather",
    "D4": "Wool",
}

countries_dict = {
    "A1": "UK",
    "A2": "France",
    "A3": "Germany",
    "A4": "Canada",
    "B1": "Spain",
    "B2": "USA",
    "B3": "Mexico",
    "B4": "China",
    "C1": "Japan",
    "C2": "Italy",
    "C3": "India",
    "C4": "Russia",
    "D1": "Brazil",
    "D2": "Australia",
    "D3": "Israel",
    "D4": "Egypt",
}

Countries_dict = {
    "A1": "UK",
    "A2": "France",
    "A3": "Germany",
    "A4": "Canada",
    "B1": "Spain",
    "B2": "USA",
    "B3": "Mexico",
    "B4": "China",
    "C1": "Japan",
    "C2": "Italy",
    "C3": "India",
    "C4": "Russia",
    "D1": "Brazil",
    "D2": "Australia",
    "D3": "Israel",
    "D4": "Egypt",
}

hobbies_dict = {
    "A1": "Stamps",
    "A2": "Fishing",
    "A3": "Sailing",
    "A4": "Cooking",
    "B1": "Trains",
    "B2": "Reading",
    "B3": "Travel",
    "B4": "Yoga",
    "C1": "Model Making",
    "C2": "Painting",
    "C3": "Walking",
    "C4": "Photography",
    "D1": "Knitting",
    "D2": "Gardening",
    "D3": "Pottery",
    "D4": "Hiking",
}

fictional_characters_dict = {
    "A1": "Hermione Granger",
    "A2": "Sherlock Holmes",
    "A3": "Dracula",
    "A4": "Wonder Woman",
    "B1": "Popeye",
    "B2": "Lara Croft",
    "B3": "Homer Simpson",
    "B4": "Tarzan",
    "C1": "Spiderman",
    "C2": "Katniss Everdeen",
    "C3": "Daenerys Targaryen",
    "C4": "Hercules",
    "D1": "Princess Leia",
    "D2": "Batman",
    "D3": "Robin Hood",
    "D4": "James Bond",
}

musical_instruments_dict = {
    "A1": "Electric Guitar",
    "A2": "Bass Guitar",
    "A3": "Clarinet",
    "A4": "Harp",
    "B1": "Piano",
    "B2": "Saxophone",
    "B3": "Trumpet",
    "B4": "Bagpipes",
    "C1": "Violin",
    "C2": "Cello",
    "C3": "Voice",
    "C4": "Harmonica",
    "D1": "Drums",
    "D2": "Flute",
    "D3": "Ukulele",
    "D4": "Banjo",
}

fairy_tales_dict = {
    "A1": "Cinderella",
    "A2": "Snow White",
    "A3": "Peter Pan",
    "A4": "Sleeping Beauty",
    "B1": "Goldilocks",
    "B2": "Rapunzel",
    "B3": "Little Red Riding Hood",
    "B4": "Hansel and Gretel",
    "C1": "Jack and the Beanstalk",
    "C2": "Aladdin",
    "C3": "Pinocchio",
    "C4": "Gingerbread Man",
    "D1": "Hare and the Tortoise",
    "D2": "Princess and the Pea",
    "D3": "Beauty and the Beast",
    "D4": "Three Little Pigs",
}

bands_dict = {
    "A1": "The Beatles",
    "A2": "Take That",
    "A3": "The Beach Boys",
    "A4": "ABBA",
    "B1": "The Rolling Stones",
    "B2": "Blondie",
    "B3": "Madonna",
    "B4": "Little Mix",
    "C1": "Fleetwood Mac",
    "C2": "Spice Girls",
    "C3": "Destiny's Child",
    "C4": "The White Stripes",
    "D1": "Nirvana",
    "D2": "Queen",
    "D3": "Jackson 5",
    "D4": "U2",
}

under_the_sea_dict = {
    "A1": "Octopus",
    "A2": "Lobster",
    "A3": "Crab",
    "A4": "Sea Turtle",
    "B1": "StarFish",
    "B2": "Seal",
    "B3": "Giant Squid",
    "B4": "Clownfish",
    "C1": "Shark",
    "C2": "Dolphin",
    "C3": "Seahorse",
    "C4": "Swordfish",
    "D1": "Jellyfish",
    "D2": "Killer Whale",
    "D3": "Stingray",
    "D4": "Mermaid",
}

DECK = CategoryDeck([
    CategoryCard("Sports Starts", sports__star_dict),
    CategoryCard("Food", food_dict),
    CategoryCard("Wedding Anniveersaries", wedding_anniversaries_dict),
    CategoryCard("Countries", countries_dict),
    CategoryCard("Hobbies", hobbies_dict),
    CategoryCard("Fictional Characters", fictional_characters_dict),
    CategoryCard("Musical Instruments", musical_instruments_dict),
    CategoryCard("Fairy Tales", fairy_tales_dict),
    CategoryCard("Bands", bands_dict),
    CategoryCard("Under The Sea", under_the_sea_dict),
]
)

