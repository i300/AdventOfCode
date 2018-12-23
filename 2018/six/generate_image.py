# fun class to generate an image from a grid

from PIL import Image, ImageDraw
import random
import solution as s

def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    
    return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]

coordinates = []
with open("six/input.txt", "r") as coordinates_file:
    coordinates = [tuple([int(x) for x in loc.strip().split(", ")]) for loc in coordinates_file.readlines()]

max_c = s.max_coords(coordinates)
img = Image.new("RGB", max_c)
draw = ImageDraw.Draw(img)

grid = s.create_grid(coordinates)

colors = get_spaced_colors(len(coordinates))
flatgrid = [y for x in grid for y in x]
for i, origin in enumerate(coordinates):
    filtered_grid = [coord for coord in flatgrid if coord[2] == origin]
    locations = [(coord[0], coord[1]) for coord in filtered_grid]
    draw.point(locations, fill=colors[i])

img.save('grid.png')