from Enums import CardColour, PlayerColor, ConnectionType

class Connection:
    def __init__(self, vertices:tuple, length:int, 
                 occupiedBy:PlayerColor=None, 
                 colour:CardColour=None,
                 connectionType:ConnectionType=None,
                 numFerries:int=None):
        
        self.vertices = vertices
        self.length = length
        self.occupiedBy = occupiedBy
        self.colour = colour
        self.connectionType = connectionType
        self.numFerries=numFerries