import random

def place_player(cave):
    player_room = random.choice(list(cave.keys()))
    return player_room

def move_player(cave, player_room):
    adjacent_rooms = cave[player_room]
    print("You can go to rooms", adjacent_rooms)
    while True:
        try:
            new_room = int(input("Which room do you want to go to? "))
            if new_room in adjacent_rooms:
                print("You are now in room", new_room)
                return new_room
            else:
                print("You can't go to that room.")
        except ValueError:
            print("Invalid input. Please enter a room number.")
