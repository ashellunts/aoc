import sys
import re

w = 101
h = 103
qw = w // 2
qh = h // 2

input = open(sys.argv[1], "r+t").read()
robots = re.findall(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)", input)
robots = [ list(map(int, r)) for r in robots ]
robots_after_100_seconds = [
    [
        (x + 100*wx) % w,
        (y + 100*wy) % h
    ]
    for x, y, wx, wy in robots
]

qlu = len([1 for x, y in robots_after_100_seconds if x < qw and y < qh ])
qru = len([1 for x, y in robots_after_100_seconds if x > qw and y < qh ])
qld = len([1 for x, y in robots_after_100_seconds if x < qw and y > qh ])
qrd = len([1 for x, y in robots_after_100_seconds if x > qw and y > qh ])

print(qlu*qru*qld*qrd == 231782040)
