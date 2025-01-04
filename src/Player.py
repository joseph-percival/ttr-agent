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

    def discardRoutes(self):
        print(f"Discard any of these routes, but keep at least one:")
        for i, card in enumerate(self.routeCards):
            if card.cardType is not CardType.LONG_ROUTE:
                print(f"{i}: {card.vertices[0].name} to {card.vertices[1].name}: {card.cardPoints} points")
            else:
                print(f"{i}: {card.vertices[0].name} to {card.vertices[1].name}: {card.cardPoints} points [LONG ROUTE - CANNOT DISCARD]")
        input()

    def playTurn(self):
        pass