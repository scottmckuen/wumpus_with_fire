import random

def place_pits(cave, num_pits):
    pit_rooms = set()
    for i in range(num_pits):
        pit_room = random.choice(list(cave.keys()))
        while pit_room in pit_rooms:
            pit_room = random.choice(list(cave.keys()))
        pit_rooms.add(pit_room)
    return pit_rooms
