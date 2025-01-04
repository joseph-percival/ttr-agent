from src.Enums import PlayerType, PlayerColour
from src.CardPile import CardPile

class Player:
    def __init__(self, colour:PlayerColour, 
                 startTrains:CardPile,
                 startRoutes:CardPile,
                 playerType:PlayerType=PlayerType.COMPUTER):
        self.colour=colour
        self.playerType=playerType
        self.trainCards=startTrains
        self.startRoutes=startRoutes
        self.score=0