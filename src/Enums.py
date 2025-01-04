from enum import Enum

class PlayerColour(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    BLACK = 3
    YELLOW = 4

class CardColour(Enum):
    LOCOMOTIVE = 0
    BLUE = 1
    RED = 2
    YELLOW = 3
    WHITE = 4
    ORANGE = 5
    GREEN = 6
    PINK = 7
    BLACK = 8

class CardType(Enum):
    TRAIN = 0,
    SHORT_ROUTE = 1,
    LONG_ROUTE = 2

class ConnectionType(Enum):
    REGULAR = 0
    WILDCARD = 1
    TUNNEL = 2
    FERRY = 3

class PlayerType(Enum):
    COMPUTER = 0
    HUMAN = 1

class City(Enum):
    AMSTERDAM = 0
    ANGORA = 1
    ATHINA = 2
    BARCELONA = 3
    BERLIN = 4
    BREST = 5
    BRINDISI = 6
    BRUXELLES = 7
    BUCURESTI = 8
    BUDAPEST = 9
    CADIZ = 10
    CONSTANTINOPLE = 11
    DANZIG = 12
    DIEPPE = 13
    EDINBURGH = 14
    ERZURUM = 15
    ESSEN = 16
    FRANKFURT = 17
    KHARKOV = 18
    KOBENHAVN = 19
    KYIV = 20
    LISBOA = 21
    LONDON = 22
    MADRID = 23
    MARSEILLE = 24
    MOSKVA = 25
    MUNCHEN = 26
    PALERMO = 27
    PAMPLONA = 28
    PARIS = 29
    PETROGRAD = 30
    RIGA = 31
    ROMA = 32
    ROSTOV = 33
    SARAJEVO = 34
    SEVASTOPOL = 35
    SMOLENSK = 36
    SMYRNA = 37
    SOCHI = 38
    SOFIA = 39
    STOCKHOLM = 40
    VENEZIA = 41
    WARSZAWA = 42
    WIEN = 43
    WILNO = 44
    ZAGRAB = 45
    ZURICH = 46