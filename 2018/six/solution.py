def manhattan_dist(location, goal):
    return abs(location[0] - goal[0]) + abs(location[1] - goal[1])

def closest_coord(loc, coordinates):
    sorted_coords = [((coord[0], coord[1]), manhattan_dist(loc, coord)) for coord in coordinates]
    sorted_coords.sort(key=lambda coord: coord[1])

    number_occrances = len([i for i,x in enumerate(sorted_coords) if x[1]==sorted_coords[0][1]])
    if (number_occrances == 1):
        return sorted_coords[0][0]
    else:
        return (-1, -1)

def print_grid(grid):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for y in range(0, max_y):
        row = ""
        for x in range(0, max_x):
            closest_coord = grid[x][y][2]
            if (closest_coord == (x, y)):
                row += "@"
            elif (closest_coord == (-1, -1)):
                row += "."
            else:
                row += alphabet[coordinates.index(grid[x][y][2])]

        print(row)

def max_coords(coordinates):
    max_x = max(coordinates, key=lambda loc: loc[0])[0] + 2
    max_y = max(coordinates, key=lambda loc: loc[1])[1] + 2
    return (max_x, max_y)

def create_grid(coordinates):
    max_c = max_coords(coordinates)

    grid = [[(x, y, 0) for y in range(0, max_c[1])] for x in range(0, max_c[0])]
    return grid

def calc_coordinate_regions(grid, coordinates):
    max_c = max_coords(coordinates)
    
    for x in range(0, max_c[0]):
        for y in range(0, max_c[1]):
            grid[x][y] = (x, y, closest_coord((x, y), coordinates))

def calc_dist_sums(grid, coordinates):
    max_c = max_coords(coordinates)

    for x in range(0, max_c[0]):
        for y in range(0, max_c[1]):
            sum_dist = sum([manhattan_dist((x, y), coord) for coord in coordinates])
            grid[x][y] = (x, y, sum_dist)

if __name__ == "__main__":
    coordinates = []
    with open("six/input.txt", "r") as coordinates_file:
        coordinates = [tuple([int(x) for x in loc.strip().split(", ")]) for loc in coordinates_file.readlines()]

    grid = create_grid(coordinates)

    max_c = max_coords(coordinates)
    max_x = max_c[0]
    max_y = max_c[1]

    # part 1
    calc_coordinate_regions(grid, coordinates)

    # create the set of coordinates that are infinite (aka those that expand outward along the sides)
    blacklist = set()
    for x in range(0, max_x):
        closest_coord_top = grid[x][0][2]
        closest_coord_bot = grid[x][max_y - 1][2]
        blacklist.add(closest_coord_bot)
        blacklist.add(closest_coord_top)

    for y in range(0, max_y):
        closest_coord_left = grid[0][y][2]
        closest_coord_right = grid[max_x - 1][y][2]
        blacklist.add(closest_coord_left)
        blacklist.add(closest_coord_right)

    # loop through grid to determine sizes of non-blacklisted coords
    coord_sizes = {}
    for x in range(0, max_x):
        for y in range(0, max_y):
            closest_coord = grid[x][y][2]
            if (closest_coord not in blacklist):
                if (closest_coord not in coord_sizes):
                    coord_sizes[closest_coord] = 0
                coord_sizes[closest_coord] += 1
    
    
    largest_coord = max(coord_sizes, key=lambda key: coord_sizes[key])
    print("Largest Coord: {}\nCoord Size: {}".format(largest_coord, coord_sizes[largest_coord]))

    # part 2
    calc_dist_sums(grid, coordinates)

    safe_region_size = 0
    for x in range(0, max_x):
        for y in range(0, max_y):
            if (grid[x][y][2] < 10000):
                safe_region_size += 1

    print("Safe Region Size: {}".format(safe_region_size))