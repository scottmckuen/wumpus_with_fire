def create_cave(num_rooms):
    cave = {}
    for room in range(1, num_rooms+1):
        cave[room] = []
    edges = [
        (1, 2), (1, 5), (1, 6), (2, 3), (2, 8),
        (3, 4), (3, 10), (4, 5), (4, 12), (5, 15),
        (6, 7), (6, 17), (7, 8), (7, 19), (8, 9),
        (9, 10), (9, 20), (10, 11), (11, 12), (11, 18),
        (12, 13), (13, 14), (13, 20), (14, 15), (14, 16),
        (15, 1), (16, 17), (16, 19), (17, 18), (18, 19)
    ]
    for edge in edges:
        cave[edge[0]].append(edge[1])
        cave[edge[1]].append(edge[0])
    return cave

