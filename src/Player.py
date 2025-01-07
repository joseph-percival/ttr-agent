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
                

    def chooseRoutes(self, newRoutes:CardPile):
        print(f"Here are your current routes:")
        self.printRoutes()
        choice = None

        while choice != "" and len(newRoutes) > 1:
            print(f"Discard any of these routes, but keep at least one:")
            self.printRoutes(cards=newRoutes)
            print("Type the number of a route you wish to discard, or press enter to skip")
            choice = input(": ")
            match choice:
                case str() if choice.isdigit() and int(choice) < len(newRoutes):
                    del newRoutes[int(choice)]
                case "":
                    break
                case _:
                    print("Invalid choice, please enter a valid route number.")
        self.routeCards.extend(newRoutes)