import math

def getChar(x, y, terrain):
    x = x % len(terrain[0])
    return terrain[y][x]

def numTrees(terrain, dx, dy):
    x, y = 0, 0
    treeCount = 0
    while y < len(terrain):
        if getChar(x, y, terrain) == '#':
            treeCount += 1
        x = x + dx
        y = y + dy
    return treeCount

with open("input.txt", "r") as terrain_file:
    terrain = [terrainLine.strip() for terrainLine in terrain_file.readlines()]
    treeCounts = [numTrees(terrain, 1, 1), numTrees(terrain, 3, 1), numTrees(terrain, 5, 1), numTrees(terrain, 7, 1), numTrees(terrain, 1, 2)]

    print("Part 1: {}".format(treeCounts[1]))
    print("Part 2: {}".format(treeCounts[0]*treeCounts[1]*treeCounts[2]*treeCounts[3]*treeCounts[4]))
