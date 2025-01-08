from src.Enums import PlayerColour, PlayerType, CardColour
from src.Board import Board
from src.Player import Player
from src.CardPile import CardPile

from random import shuffle
from collections import deque

class TicketToRideGame:
    def __init__(self, playerList:list=None):
        self.board = Board()
        self.players=deque()
        self.lowestTrains=45

        for colour in PlayerColour:
            if colour.name in playerList:
                self.players.appendleft(Player(colour=colour, playerType=PlayerType.HUMAN))
            else:
                self.players.appendleft(Player(colour=colour))

        # begin setup
        shuffle(self.board.routePile)
        shuffle(self.board.longRoutePile)
        shuffle(self.board.trainPile)

        # distribute starting cards
        for player in self.players:
            player.routeCards.extend(self.board.drawCards(1,"longRoutePile"))
            player.trainCards.extend(self.board.drawCards(4,"trainPile"))
            newRouteCards = self.board.drawCards(3,"routePile")

            print(f"-- {player.colour.name} --")
            self.chooseRoutes(player, newRouteCards)

        self.board.trainPool.extend(self.board.drawCards(5,"trainPile"))

        # game loop
        while self.lowestTrains > 2: # make sure you loop back round at the end
            # player at deque 0 makes turn
            current = self.players[0]
            for connection in self.board.connections:
                print(f"{connection.occupiedBy}: {connection.vertices[0].name} to {connection.vertices[1].name}: {connection.length}, {connection.colour}, {connection.connectionType.name}")
            self.playTurn(current)
            # turn of play rotates
            self.players.rotate(-1)
            self.lowestTrains = min(self.lowestTrains, current.numTrains)
            input("next turn")

        # everyone from 0 to end of deque -1 gets another turn
        for player in self.players[:-1]:
            self.playTurn(player)

    def playTurn(self, player:Player):
        print(f"{player.colour.name}'s turn: choose an action")
        choice = ""
        while choice == "":
            choice = input(": ")
            match choice:
                case "1":
                    # draw train cards
                    player.printTrainCards()
                    self.drawTrainCards(player)
                case "2":
                    # play a route
                    self.playRoute()
                case "3":
                    # place a station
                    self.placeStation()
                case "4":
                    # draw route cards
                    newRouteCards = self.board.drawCards(3, "routePile")
                    self.chooseRoutes(player, newRouteCards)
                case _:
                    choice = ""
                    print("invalid choice")

    def chooseRoutes(self, player:Player, newRoutes:CardPile):
        print(f"Here are your current routes:")
        player.printRoutes()
        choice = None

        while choice != "" and len(newRoutes) > 1:
            print(f"Discard any of these routes, but keep at least one:")
            player.printRoutes(cards=newRoutes)
            print("Type the number of a route you wish to discard, or press enter to skip")
            choice = input(": ")
            match choice:
                case str() if choice.isdigit() and int(choice) < len(newRoutes):
                    del newRoutes[int(choice)] # TODO: move to discard pile instead
                case "":
                    break
                case _:
                    print("Invalid choice, please enter a valid route number.")
        player.routeCards.extend(newRoutes)
        
    def drawTrainCards(self, player):
        print("Choose any two cards from the train pool by typing the corrseponding number")
        print("Or, type x to select a card from the deck")
        print("If you choose a locomotive card from the pool you may not draw another card")
        cards = []
        while len(cards) < 2:
            self.board.printTrainPool()
            print("Type the number of a train you wish to pick, or enter x to draw from the deck")
            choice = input(": ")
            match choice:
                case str() if choice.isdigit() and int(choice) < len(self.board.trainPool):
                    card = self.board.trainPool[int(choice)]
                    cards.append(card)
                    del self.board.trainPool[int(choice)]
                    # TODO: handle locomotives
                    # if card.cardType is CardColour.LOCOMOTIVE:
                    #     break
                case "x":
                    cards.extend(self.board.drawCards(1, "trainPile"))
                case _:
                    print("Invalid choice, please enter a valid route number.")

        player.trainCards.extend(cards)
        player.printTrainCards()

    def playRoute(self):
        pass

    def placeStation(self):
        pass