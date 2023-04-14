import random

def place_wumpus(cave, player_room):
    wumpus_room = random.choice(list(cave.keys()))
    while wumpus_room == player_room:
        wumpus_room = random.choice(list(cave.keys()))
    return wumpus_room
