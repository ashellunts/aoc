import sys
import re

w = 101
h = 103
qw = w // 2
qh = h // 2

input = open(sys.argv[1], "r+t").read()
robots = re.findall(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)", input)
robots = [ list(map(int, r)) for r in robots ]

def symmetric_map(robots_map, i, j, w, h):
    symmetric = True
    for line in robots_map[i:i+h]:
        line = line[j:j+w]
        left = line[0:qw]
        right = line[qw+1:]
        if left != right[::-1]:
            symmetric = False
            break
    return symmetric

from PIL import Image

def draw_robot_map(robots_map, w, h, output_file):
    # Create a new image with white background
    image = Image.new("RGB", (w, h), "white")
    pixels = image.load()

    # Set pixel to black for robots
    for y in range(h):
        for x in range(w):
            if robots_map[y][x]:
                pixels[x, y] = (0, 0, 0)  # Black for robot

    # Save the image to file
    image.save(output_file)

seconds = 0
while True:
    robots_map = [[False for _ in range(w)] for _ in range(h)]

    overlap = False
    for x, y, wx, wy in robots:
        newx = (x + wx*seconds) % w
        newy = (y + wy*seconds) % h

        if robots_map[newy][newx]:
            overlap = True
            break
        else:
            robots_map[newy][newx] = True

    print(seconds)
    if not overlap:
        break
    # draw_robot_map(robots_map, w, h, f"robots_map_{seconds}.png")
    seconds += 1
