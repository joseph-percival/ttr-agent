from src.Enums import PlayerType, PlayerColour, CardType
from src.CardPile import CardPile

class Player:
    def __init__(self, colour:PlayerColour, 
                 playerType:PlayerType=PlayerType.COMPUTER):
        self.colour=colour
        self.playerType=playerType
        self.trainCards=CardPile()
        self.routeCards=CardPile()
        self.score=0
        self.numTrains=45
        self.numStations=3

    def printRoutes(self, cards:CardPile=None):
        cards = self.routeCards if cards == None else cards
        for i, card in enumerate(cards):
            match card.cardType:
                case CardType.LONG_ROUTE:
                    print(f"{i}: {card.vertices[0].name} to {card.vertices[1].name}: {card.cardPoints} points [LONG ROUTE]")
                case _:
                    print(f"{i}: {card.vertices[0].name} to {card.vertices[1].name}: {card.cardPoints} points")

    def printTrainCards(self):
        for i, card in enumerate(self.trainCards):
            print(f"{i}: {card.cardColour.name} ")
                