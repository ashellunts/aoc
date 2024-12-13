import re
from dataclasses import dataclass

@dataclass
class M:
    ax: int
    ay: int
    bx: int
    by: int
    prizex: int
    prizey: int

import sys
f = open(sys.argv[1], "r+t")

ms = []

while True:
    line = f.readline()
    if not line:
        break
    if (line.strip() == ""):
        continue
    pattern = r"(Button \w+):\s*X\+(\d+),\s*Y\+(\d+)"
    match = re.search(pattern, line)
    ax = int(match.group(2))  # X value
    ay = int(match.group(3))  # Y value

    line = f.readline()
    pattern = r"(Button \w+):\s*X\+(\d+),\s*Y\+(\d+)"
    match = re.search(pattern, line)
    bx = int(match.group(2))  # X value
    by = int(match.group(3))  # Y value

    line = f.readline()
    pattern = r"X=(\d+),\s*Y=(\d+)"
    match = re.search(pattern, line)
    prizex = int(match.group(1)) + 10000000000000
    prizey = int(match.group(2)) + 10000000000000
    ms.append(M(ax, ay, bx, by, prizex, prizey))

def is_natural_number(num):
    return (isinstance(num, int) or (isinstance(num, float) and num.is_integer())) and num >= 0

tokens = 0

for m in ms:
    pressb = (-m.ay*m.prizex + m.ax*m.prizey)/(-m.ay*m.bx + m.ax*m.by)
    pressa = (m.prizey - m.by*pressb)/m.ay

    if not is_natural_number(pressa) or not is_natural_number(pressb):
        continue

    tokens += pressa*3+pressb
    print(pressa, pressb, tokens)


print(tokens)

# ax*n + bx*m = prizex
# ay*n + by*m = prizey

# n = (prizex - bx*m)/ax
# ay/ax*(prizex - bx*m) + by*m = prizey

# ay/ax*prizex - ay/ax*bx*m + by*m - prizey = 0

# m(-ay/ax*bx + by) = -ay/ax*prizex + prizey

# m = (-ay*prizex + ax*prizey)/(-ay*bx + ax*by)

# n = (prizey - by*m)/ay
