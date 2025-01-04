from src.Enums import CardType, CardColour

class Card:
    def __init__(self, cardType:CardType, 
                 cardColour:CardColour=None,
                 cardPoints:int=None, 
                 vertices:tuple=None):
        self.cardType=cardType
        self.cardColour=cardColour
        self.cardPoints=cardPoints
        self.vertices=vertices