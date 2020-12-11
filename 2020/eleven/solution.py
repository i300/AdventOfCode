import copy

def lookup(map, x, y):
    if (x < 0) or (x >= len(map[0])) or (y < 0) or (y >= len(map)):
        return None
    else:
        return map[y][x]

def num_neighbors_direct(map, x, y):
    num = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (dx == 0 and dy == 0):
                continue
            if lookup(map, x + dx, y + dy) == '#':
                num += 1
    
    return num

def num_neighbors_vision(map, x, y):
    num = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (dx == 0 and dy == 0):
                continue
            wx = x + dx
            wy = y + dy
            while True:
                result = lookup(map, wx, wy)
                if (result == None):
                    break
                elif (result == 'L'):
                    break
                elif (result == '#'):
                    num += 1
                    break
                else:
                    wx += dx
                    wy += dy
    return num


def print_map(map):
    for line in map:
        print(line)
    print(" ")

def tick_gol(map, num_neighbors, tolerance):
    newmap = copy.deepcopy(map)
    for y, line in enumerate(map):
        for x, status in enumerate(line):
            n = num_neighbors(map, x, y)
            if status == '#' and n >= tolerance:
                newmap[y][x] = 'L'
            elif status == 'L' and n == 0:
                newmap[y][x] = '#'

    return newmap

def find_stability(map, num_neighbors=num_neighbors_direct, tolerance=4, print=False):
    while True:
        newmap = tick_gol(map, num_neighbors, tolerance)
        if newmap == map:
            return map
        map = newmap
        if print:
            print_map(map)

with open('input.txt', 'r') as input_file:
    map = [[c for c in line.strip()] for line in input_file.readlines()]

    stable_map1 = find_stability(map)
    stable_map2 = find_stability(map, num_neighbors_vision, 5)
    num_occupied1 = sum([len([x for x in line if x == '#']) for line in stable_map1])
    num_occupied2 = sum([len([x for x in line if x == '#']) for line in stable_map2])
    print('Part 1: {}'.format(num_occupied1))
    print('Part 2: {}'.format(num_occupied2))
