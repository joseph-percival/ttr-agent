from src.Enums import CardColour, PlayerColour, ConnectionType

class Connection:
    def __init__(self, vertices:tuple, length:int, 
                 occupiedBy:PlayerColour=None, 
                 colour:CardColour=None,
                 connectionType:ConnectionType=None,
                 numFerries:int=None):
        
        self.vertices = vertices
        self.length = length
        self.occupiedBy = occupiedBy
        self.colour = colour
        self.connectionType = connectionType
        self.numFerries=numFerries