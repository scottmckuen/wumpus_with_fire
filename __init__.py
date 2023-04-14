import random
from cave import create_cave
from player import place_player, move_player
from wumpus import place_wumpus
from pits import place_pits

cave = create_cave(20)  # creates a cave with 20 rooms
player_room = place_player(cave)
wumpus_room = place_wumpus(cave, player_room)
pit_rooms = place_pits(cave, 3)

while True:
    adjacent_rooms = cave[player_room]
    print("You are in room", player_room)
    two_away_rooms = set(adjacent_rooms)
    for room in adjacent_rooms:
        two_away_rooms.update(cave[room])
    if wumpus_room in two_away_rooms:
        print("You smell a terrible stench.")
    if any(pit_room in adjacent_rooms for pit_room in pit_rooms):
        print("You feel a draft.")
    player_room = move_player(cave, player_room)
    if player_room == wumpus_room:
        print("You were eaten by the wumpus! Game over.")
        break
    if player_room in pit_rooms:
        print("You fell into a pit! Game over.")
        break
    if random.random() < 0.2:
        wumpus_adjacent_rooms = cave[wumpus_room]
        wumpus_room = random.choice(wumpus_adjacent_rooms)
        if wumpus_room == player_room:
            print("The wumpus ate you! Game over.")
            break
        print("You hear a faint sound.")
