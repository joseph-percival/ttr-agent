from Card import Card
from collections import deque

class CardPile(deque):
    def __init__(self, startPile:list=None):
        self = super(startPile)