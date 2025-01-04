# Board
from Enums import ConnectionType, City, CardColour, CardType
from Connection import Connection
from Card import Card
from CardPile import CardPile

class Board:
    def __init__(self):
        # define all connections between cities
        self.connections = {
            Connection((City.EDINBURGH,City.LONDON), 4, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.EDINBURGH,City.LONDON), 4, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR)
        }

        # map route length to points gained
        self.lengthPoints = {
            1:1,
            2:2,
            3:4,
            4:7,
            6:15,
            8:21
        }

        # stub card hands
        self.trainDiscard = CardPile()
        self.routeDiscard = CardPile()
        self.longRoutePile = CardPile(startPile=[
            Card(cardType=CardType.LONG_ROUTE, cardPoints=21, vertices=(City.EDINBURGH,City.ATHINA))
        ])
        self.routePile = CardPile(startPile=[
            Card(cardType=CardType.SHORT_ROUTE, cardPoints=1, vertices=(City.EDINBURGH,City.ATHINA))
        ])
        self.trainPile = CardPile(startPile=[
            Card(cardType=CardType.TRAIN, cardColour=CardColour.RED)
        ])
        self.trainHand = CardPile(startPile=[
            Card(cardType=CardType.TRAIN, cardColour=CardColour.RED)
        ])

