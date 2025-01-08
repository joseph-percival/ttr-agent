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
    WILDCARD = 1 # currently unused (represents grey routes)
    TUNNEL = 2
    FERRY = 3

class PlayerType(Enum):
    COMPUTER = 0
    HUMAN = 1

class City(Enum):
    AMSTERDAM = (1320, -951)
    ANGORA = (3417, -2460)
    ATHINA = (2645, -2460)
    BARCELONA = (934, -2332)
    BERLIN = (1990, -1033)
    BREST = (610, -1380)
    BRINDISI = (2193, -2172)
    BRUXELLES = (1234, -1123)
    BUCURESTI = (2938, -1798)
    BUDAPEST = (2368, -1552)
    CADIZ = (516, -2585)
    CONSTANTINOPLE = (3133, -2258)
    DANZIG = (2400, -749)
    DIEPPE = (930, -1275)
    EDINBURGH = (723, -386)
    ERZURUM = (3721, -2355)
    ESSEN = (1620, -979)
    FRANKFURT = (1573, -1236)
    KHARKOV = (3651, -1361)
    KOBENHAVN = (1889, -593)
    KYIV = (3144, -1182)
    LISBOA = (278, -2386)
    LONDON = (969, -940)
    MADRID = (532, -2301)
    MARSEILLE = (1440, -1973)
    MOSKVA = (3694, -803)
    MUNCHEN = (1784, -1400)
    PALERMO = (2021, -2558)
    PAMPLONA = (891, -1993)
    PARIS = (1117, -1427)
    PETROGRAD = (3333, -363)
    RIGA = (2700, -398)
    ROMA = (1881, -2071)
    ROSTOV = (3807, -1560)
    SARAJEVO = (2470, -2000)
    SEVASTOPOL = (3452, -1844)
    SMOLENSK = (3370, -901)
    SMYRNA = (2977, -2542)
    SOCHI = (3792, -1891)
    SOFIA = (2712, -2028)
    STOCKHOLM = (2244, -293)
    VENEZIA = (1854, -1747)
    WARSZAWA = (2583, -990)
    WIEN = (2193, -1443)
    WILNO = (2996, -897)
    ZAGRAB = (2158, -1790)
    ZURICH = (1538, -1630)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @property
    def coordinates(self):
        return (self.latitude, self.longitude)