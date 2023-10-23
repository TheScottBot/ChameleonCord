from models import PlayerDeck, PlayerCard

green_dict = {
    "One.1": "B1",
    "One.2": "B2",
    "One.3": "D2",
    "One.4": "A3",
    "One.5": "A2",
    "One.6": "A1",
    "One.7": "A3",
    "One.8": "C1",

    "Two.1": "C4",
    "Two.2": "D1",
    "Two.3": "A4",
    "Two.4": "C1",
    "Two.5": "C4",
    "Two.6": "C2",
    "Two.7": "A3",
    "Two.8": "B3",

    "Three.1": "B1",
    "Three.2": "D1",
    "Three.3": "B2",
    "Three.4": "D4",
    "Three.5": "B4",
    "Three.6": "A4",
    "Three.7": "B1",
    "Three.8": "B2",

    "Four.1": "A2",
    "Four.2": "D2",
    "Four.3": "A2",
    "Four.4": "C2",
    "Four.5": "D2",
    "Four.6": "C1",
    "Four.7": "C2",
    "Four.8": "D3",

    "Five.1": "D4",
    "Five.2": "B3",
    "Five.3": "B3",
    "Five.4": "A4",
    "Five.5": "C3",
    "Five.6": "B4",
    "Five.7": "C4",
    "Five.8": "A1",

    "Six.1": "C3",
    "Six.2": "D1",
    "Six.3": "D4",
    "Six.4": "B4",
    "Six.5": "C3",
    "Six.6": "D3",
    "Six.7": "A1",
    "Six.8": "D2",
}

blue_dict = {
    "One.1": "D4",
    "One.2": "A2",
    "One.3": "C3",
    "One.4": "B3",
    "One.5": "D2",
    "One.6": "A1",
    "One.7": "D3",
    "One.8": "B4",

    "Two.1": "B2",
    "Two.2": "A4",
    "Two.3": "D3",
    "Two.4": "D2",
    "Two.5": "A2",
    "Two.6": "B4",
    "Two.7": "B4",
    "Two.8": "C4",

    "Three.1": "C2",
    "Three.2": "D3",
    "Three.3": "A2",
    "Three.4": "B1",
    "Three.5": "C2",
    "Three.6": "A4",
    "Three.7": "C1",
    "Three.8": "B2",

    "Four.1": "A3",
    "Four.2": "A1",
    "Four.3": "B1",
    "Four.4": "D4",
    "Four.5": "A3",
    "Four.6": "B2",
    "Four.7": "D4",
    "Four.8": "D2",

    "Five.1": "C1",
    "Five.2": "C3",
    "Five.3": "A3",
    "Five.4": "A4",
    "Five.5": "B3",
    "Five.6": "C3",
    "Five.7": "C1",
    "Five.8": "D1",

    "Six.1": "B3",
    "Six.2": "D1",
    "Six.3": "C4",
    "Six.4": "A1",
    "Six.5": "B1",
    "Six.6": "C2",
    "Six.7": "C4",
    "Six.8": "D1",
}

DECK = PlayerDeck([
    PlayerCard("green", green_dict),
    PlayerCard("blue", blue_dict)
    ]
)


