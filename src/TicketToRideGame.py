from src.Enums import PlayerColour, PlayerType
from src.Board import Board
from src.Player import Player

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
            player.routeCards.append(self.board.longRoutePile.pop())
            for _ in range(3):
                player.routeCards.append(self.board.routePile.pop())
            for _ in range(4):
                player.trainCards.append(self.board.trainPile.pop())
            player.discardRoutes()
        for _ in range(5):
            self.board.trainPool.append(self.board.trainPile.pop())

        # game loop
        while self.lowestTrains > 2: # make sure you loop back round at the end
            # player at deque 0 makes turn
            current = self.players[0]
            for connection in self.board.connections:
                print(f"{connection.occupiedBy}: {connection.vertices[0].name} to {connection.vertices[1].name}: {connection.length}, {connection.colour}, {connection.connectionType.name}")
            current.playTurn()
            # turn of play rotates
            self.players.rotate(-1)
            self.lowestTrains = min(self.lowestTrains, current.numTrains)
            input("next turn")

        # everyone from 0 to end of deque -1 gets another turn
        for player in self.players[:-1]:
            player.playTurn()

        