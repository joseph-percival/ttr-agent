from src.TicketToRideGame import TicketToRideGame

import sys

# usage:
# python3 main.py
# (computer players only)

# python3 main.py <HUMAN_COLOUR> <HUMAN_COLOUR> [...]
# add human players 
# allowed colours: RED BLUE GREEN YELLOW BLACK
if __name__ == "__main__":
    print(sys.argv)
    playerColours = (
        "RED",
        "BLUE",
        "GREEN",
        "YELLOW",
        "BLACK"
    )
    assert len(sys.argv) <= 6 # TOO MANY ARGUMENTS
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            assert(item in playerColours) # PLAYER COLOUR NOT RECOGNISED
    print("setting up game")

    game = TicketToRideGame(sys.argv[1:])
