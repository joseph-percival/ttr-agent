# Board
from src.Enums import ConnectionType, City, CardColour, CardType
from src.Connection import Connection
from src.Card import Card
from src.CardPile import CardPile

class Board:
    def __init__(self):
        # define all connections between cities
        self.connections = {
            Connection((City.EDINBURGH,City.LONDON), 4, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.EDINBURGH,City.LONDON), 4, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.LONDON,City.AMSTERDAM), 2, numFerries=2, connectionType=ConnectionType.FERRY),
            Connection((City.LONDON,City.DIEPPE), 2, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.LONDON,City.DIEPPE), 2, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.DIEPPE,City.BREST), 2, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.DIEPPE,City.BRUXELLES), 2, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.DIEPPE,City.PARIS), 1, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.BREST,City.PARIS), 3, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.BREST,City.PAMPLONA), 4, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.PAMPLONA,City.PARIS), 4, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.PAMPLONA,City.PARIS), 4, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.PAMPLONA,City.MADRID), 3, colour=CardColour.WHITE, connectionType=ConnectionType.TUNNEL),
            Connection((City.PAMPLONA,City.MADRID), 3, colour=CardColour.BLACK, connectionType=ConnectionType.TUNNEL),
            Connection((City.PAMPLONA,City.BARCELONA), 2, connectionType=ConnectionType.TUNNEL),
            Connection((City.PAMPLONA,City.MARSEILLE), 4, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.MADRID,City.LISBOA), 3, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.MADRID,City.CADIZ), 3, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.MADRID,City.BARCELONA), 2, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.LISBOA,City.CADIZ), 2, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.BARCELONA,City.MARSEILLE), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.PARIS,City.BRUXELLES), 2, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.PARIS,City.BRUXELLES), 2, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.PARIS,City.FRANKFURT), 3, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.PARIS,City.FRANKFURT), 3, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.PARIS,City.ZURICH), 3, connectionType=ConnectionType.TUNNEL),
            Connection((City.PARIS,City.MARSEILLE), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.ZURICH,City.MARSEILLE), 2, colour=CardColour.PINK, connectionType=ConnectionType.TUNNEL),
            Connection((City.ZURICH,City.VENEZIA), 2, colour=CardColour.GREEN, connectionType=ConnectionType.TUNNEL),
            Connection((City.ZURICH,City.MUNCHEN), 2, colour=CardColour.YELLOW, connectionType=ConnectionType.TUNNEL),
            Connection((City.MARSEILLE,City.ROMA), 4, connectionType=ConnectionType.TUNNEL),
            Connection((City.BRUXELLES,City.AMSTERDAM), 1, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.BRUXELLES,City.FRANKFURT), 2, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.AMSTERDAM,City.FRANKFURT), 2, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.AMSTERDAM,City.ESSEN), 3, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.FRANKFURT,City.ESSEN), 2, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.FRANKFURT,City.MUNCHEN), 2, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.FRANKFURT,City.BERLIN), 3, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.FRANKFURT,City.BERLIN), 3, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.ESSEN,City.BERLIN), 2, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.ESSEN,City.KOBENHAVN), 3, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.ESSEN,City.KOBENHAVN), 3, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.KOBENHAVN,City.STOCKHOLM), 3, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.KOBENHAVN,City.STOCKHOLM), 3, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.STOCKHOLM,City.PETROGRAD), 8, connectionType=ConnectionType.TUNNEL),
            Connection((City.MUNCHEN,City.WIEN), 3, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.MUNCHEN,City.VENEZIA), 2, colour=CardColour.BLUE, connectionType=ConnectionType.TUNNEL),
            Connection((City.VENEZIA,City.ZAGRAB), 2, connectionType=ConnectionType.REGULAR),
            Connection((City.VENEZIA,City.ROMA), 2, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.ROMA,City.BRINDISI), 2, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.ROMA,City.PALERMO), 4, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.PALERMO,City.BRINDISI), 3, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.PALERMO,City.SMYRNA), 6, numFerries=2, connectionType=ConnectionType.FERRY),
            Connection((City.BRINDISI,City.ATHINA), 4, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.BERLIN,City.DANZIG), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.BERLIN,City.WARSZAWA), 4, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.BERLIN,City.WARSZAWA), 4, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.BERLIN,City.WIEN), 3, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.WIEN,City.ZAGRAB), 2, connectionType=ConnectionType.REGULAR),
            Connection((City.WIEN,City.BUDAPEST), 1, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.WIEN,City.BUDAPEST), 1, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.WIEN,City.WARSZAWA), 4, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.ZAGRAB,City.BUDAPEST), 2, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.ZAGRAB,City.SARAJEVO), 3, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.DANZIG,City.RIGA), 3, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.DANZIG,City.WARSZAWA), 2, connectionType=ConnectionType.REGULAR),
            Connection((City.BUDAPEST,City.SARAJEVO), 3, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.BUDAPEST,City.BUCURESTI), 4, connectionType=ConnectionType.TUNNEL),
            Connection((City.BUDAPEST,City.KYIV), 6, connectionType=ConnectionType.TUNNEL),
            Connection((City.SARAJEVO,City.ATHINA), 4, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.SARAJEVO,City.SOFIA), 2, connectionType=ConnectionType.TUNNEL),
            Connection((City.WARSZAWA,City.WILNO), 3, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.WARSZAWA,City.KYIV), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.ATHINA,City.SOFIA), 3, colour=CardColour.PINK, connectionType=ConnectionType.REGULAR),
            Connection((City.ATHINA,City.SMYRNA), 1, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.SOFIA,City.BUCURESTI), 2, connectionType=ConnectionType.TUNNEL),
            Connection((City.SOFIA,City.CONSTANTINOPLE), 3, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.RIGA,City.PETROGRAD), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.RIGA,City.WILNO), 4, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.BUCURESTI,City.KYIV), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.BUCURESTI,City.SEVASTOPOL), 4, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.BUCURESTI,City.CONSTANTINOPLE), 3, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.SMYRNA,City.CONSTANTINOPLE), 2, colour=CardColour.YELLOW, connectionType=ConnectionType.TUNNEL),
            Connection((City.SMYRNA,City.ANGORA), 3, colour=CardColour.ORANGE, connectionType=ConnectionType.TUNNEL),
            Connection((City.WILNO,City.PETROGRAD), 4, colour=CardColour.BLUE, connectionType=ConnectionType.REGULAR),
            Connection((City.WILNO,City.SMOLENSK), 3, colour=CardColour.YELLOW, connectionType=ConnectionType.REGULAR),
            Connection((City.WILNO,City.KYIV), 2, connectionType=ConnectionType.REGULAR),
            Connection((City.CONSTANTINOPLE,City.SEVASTOPOL), 4, numFerries=2, connectionType=ConnectionType.FERRY),
            Connection((City.CONSTANTINOPLE,City.ANGORA), 2, connectionType=ConnectionType.TUNNEL),
            Connection((City.PETROGRAD,City.MOSKVA), 4, colour=CardColour.WHITE, connectionType=ConnectionType.REGULAR),
            Connection((City.KYIV,City.SMOLENSK), 3, colour=CardColour.RED, connectionType=ConnectionType.REGULAR),
            Connection((City.KYIV,City.KHARKOV), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.SMOLENSK,City.MOSKVA), 2, colour=CardColour.ORANGE, connectionType=ConnectionType.REGULAR),
            Connection((City.ANGORA,City.ERZURUM), 3, colour=CardColour.BLACK, connectionType=ConnectionType.REGULAR),
            Connection((City.SEVASTOPOL,City.ERZURUM), 4, numFerries=2, connectionType=ConnectionType.FERRY),
            Connection((City.SEVASTOPOL,City.SOCHI), 2, numFerries=1, connectionType=ConnectionType.FERRY),
            Connection((City.SEVASTOPOL,City.ROSTOV), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.KHARKOV,City.MOSKVA), 4, connectionType=ConnectionType.REGULAR),
            Connection((City.KHARKOV,City.ROSTOV), 2, colour=CardColour.GREEN, connectionType=ConnectionType.REGULAR),
            Connection((City.ERZURUM,City.SOCHI), 3, colour=CardColour.RED, connectionType=ConnectionType.TUNNEL),
            Connection((City.SOCHI,City.ROSTOV), 2, connectionType=ConnectionType.REGULAR),
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

        # setup card hands
        self.trainDiscard = CardPile()
        self.routeDiscard = CardPile()

        self.trainPool = CardPile()

        self.routePile = CardPile(startPile=[
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ATHINA, City.ANGORA), cardPoints= 5),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BUDAPEST, City.SOFIA), cardPoints= 5),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.FRANKFURT, City.KOBENHAVN), cardPoints= 5),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ROSTOV, City.ERZURUM), cardPoints= 5),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.SOFIA, City.SMYRNA), cardPoints= 5),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.KYIV, City.PETROGRAD), cardPoints= 6),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ZURICH, City.BRINDISI), cardPoints= 6),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ZURICH, City.BUDAPEST), cardPoints= 6),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.WARSZAWA, City.SMOLENSK), cardPoints= 6),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ZAGRAB, City.BRINDISI), cardPoints= 6),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.PARIS, City.ZAGRAB), cardPoints= 7),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BREST, City.MARSEILLE), cardPoints= 7),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.LONDON, City.BERLIN), cardPoints= 7),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.EDINBURGH, City.PARIS), cardPoints= 7),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.AMSTERDAM, City.PAMPLONA), cardPoints= 7),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ROMA, City.SMYRNA), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.PALERMO, City.CONSTANTINOPLE), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.SARAJEVO, City.SEVASTOPOL), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.MADRID, City.DIEPPE), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BARCELONA, City.BRUXELLES), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.PARIS, City.WIEN), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BARCELONA, City.MUNCHEN), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BREST, City.VENEZIA), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.SMOLENSK, City.ROSTOV), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.MARSEILLE, City.ESSEN), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.KYIV, City.SOCHI), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.MADRID, City.ZURICH), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BERLIN, City.BUCURESTI), cardPoints= 8),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BRUXELLES, City.DANZIG), cardPoints= 9),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BERLIN, City.ROMA), cardPoints= 9),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ANGORA, City.KHARKOV), cardPoints= 10),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.RIGA, City.BUCURESTI), cardPoints= 10),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ESSEN, City.KYIV), cardPoints= 10),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.VENEZIA, City.CONSTANTINOPLE), cardPoints= 10),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.LONDON, City.WIEN), cardPoints= 10),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.ATHINA, City.WILNO), cardPoints= 11),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.STOCKHOLM, City.WIEN), cardPoints= 11),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.BERLIN, City.MOSKVA), cardPoints= 12),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.AMSTERDAM, City.WILNO), cardPoints= 12),
            Card(cardType=CardType.SHORT_ROUTE, vertices=(City.FRANKFURT, City.SMOLENSK), cardPoints= 13)
        ])

        self.longRoutePile = CardPile(startPile=[
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.LISBOA, City.DANZIG), cardPoints= 20),
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.BREST, City.PETROGRAD), cardPoints= 20),
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.PALERMO, City.MOSKVA), cardPoints= 20),
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.KOBENHAVN, City.ERZURUM), cardPoints= 21),
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.EDINBURGH, City.ATHINA), cardPoints= 21),
            Card(cardType=CardType.LONG_ROUTE, vertices=(City.CADIZ, City.STOCKHOLM), cardPoints= 21)
        ])

        self.trainPile = CardPile(startPile=[
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.LOCOMOTIVE) for _ in range(14)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.BLUE) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.RED) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.YELLOW) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.WHITE) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.ORANGE) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.GREEN) for _ in range(12)]),
            *([Card(cardType=CardType.TRAIN, cardColour=CardColour.PINK) for _ in range(12)])
        ])

        # city:(playerColour,connectingCity)
        self.placedStations = {}

    def printTrainPool(self):
        for i, card in enumerate(self.trainPool):
            print(f"{i}: {card.cardColour.name} ")

    def drawCards(self, num:int, deck:str):
        out = []
        for _ in range(num):
            eval(f"out.append(self.{deck}.popleft())")
        return out
        # TODO: handle running out of cards
            