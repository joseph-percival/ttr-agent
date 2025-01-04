from collections import deque

class CardPile(deque):
    def __init__(self, startPile:list=None):
        super().__init__(startPile if startPile else [])