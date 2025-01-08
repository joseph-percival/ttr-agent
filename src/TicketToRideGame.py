from src.Enums import PlayerColour, PlayerType, City
from src.Board import Board
from src.Player import Player
from src.CardPile import CardPile

from random import shuffle
from collections import deque

import matplotlib.pyplot as plt

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

        self.displayBoard()
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
            # self.displayBoard()
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
                    self.placeStation(player)
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
                    self.board.routeDiscard.append(newRoutes[int(choice)])
                    del newRoutes[int(choice)]
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
        while len(self.board.trainPool) < 5:
            self.board.trainPool.extend(self.board.drawCards(1,"trainPile"))
        player.trainCards.extend(cards)
        player.printTrainCards()

    def playRoute(self):
        pass

    def placeStation(self, player):
        print("Type a city name to place a station")
        print("You cannot choose a city that already has a station attched")
        print("Type the city name you wish to pick")
        requiredCards = 4 - player.numStations
        while True:
            choice = input(": ")
            match choice:
                case str() if choice in City._member_names_ and choice not in self.board.placedStations:
                    city = choice
                    # TODO: lookup of destination city
                    self.board.placedStations[city] = (PlayerColour, destinationCity)
                    break
                case _:
                    print("Invalid choice, please enter a valid city.")
            
        print("Select which card(s) you would like to exchange")
        while True:
            print("Your current cards: ")
            player.printTrainCards()
            print("Colours avaliable to exchange: ")
            colours = [card.cardColour for card in player.trainCards]
            colours = set([colour.name for colour in colours if colours.count(colour)>=requiredCards])
            for i, colour in enumerate(colours):
                print(f"{i}: {colour}")
            choice = input(": ")
            match choice:
                case str() if choice.isdigit() and int(choice) < len(colours):
                    colour = colours[int(choice)]
                    # player.trainCards.remove() TODO: remove cards by colour
                    break
                case _:
                    print("Invalid choice, please enter a valid card colour.")

        player.numStations -= 1

    def displayBoard(self):
        plt.ion()
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_title("Ticket to Ride Board")
        ax.set_facecolor("beige")
        # plot cities
        for city in City:
            x, y = city.coordinates
            ax.scatter(x, y, label=city.name, color='blue')
            ax.text(x + 0.05, y, city.name, fontsize=9)
        # plot connections
        for connection in self.board.connections:
            x1, y1 = connection.vertices[0].coordinates
            x2, y2 = connection.vertices[1].coordinates
            try:
                ax.plot([x1, x2], [y1, y2], color=connection.colour.name.lower(), linewidth=2)
            except:
                ax.plot([x1, x2], [y1, y2], color='gray', linewidth=2)
        # plot stations
        for city_name, (player_colour, _) in self.board.placedStations.items():
            city = City[city_name]
            x, y = city.coordinates
            ax.scatter(x, y, color=player_colour.name.lower(), s=100, marker='s')
        
        plt.show()