with open("test2.txt", "r+t") as f:
    lines = f.readlines()

n = len(lines)
m = len(lines[0].strip())

map = [[{} for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        map[i][j] = {
            "type": lines[i][j],
            "regionID": -1,
            "calculated": False
        }

def indexInMap(i, j):
    return (0 <= i < n) and (0 <= j < m)

regionIDLocation = {}

def depthSearch(i, j, t):
    if not indexInMap(i, j):
        return
    if map[i][j]["regionID"] != -1:
        return
    if map[i][j]["type"] != t:
        return
    map[i][j]["regionID"] = currentRegionID
    regionIDLocation[currentRegionID] = i, j
    depthSearch(i + 1, j, t)
    depthSearch(i - 1, j, t)
    depthSearch(i, j + 1, t)
    depthSearch(i, j - 1, t)


def findNextNotVisitedPlot():
    for i in range(n):
        for j in range(m):
            if map[i][j]["regionID"] == -1:
                return i, j, map[i][j]["type"]
    return None

def printMap():
    for i in range(n):
        for j in range(m):
            print(map[i][j]["regionID"], end='')
            print(" ", end='')
        print("")

currentRegionID = -1
while True:
    nextNotVisitedPlot = findNextNotVisitedPlot()
    if not nextNotVisitedPlot:
        break
    i, j, t = nextNotVisitedPlot
    currentRegionID += 1
    # print("next plot not visited ", i, j, t)
    # print("use regionID ", currentRegionID)
    depthSearch(i, j, t)
    # printMap()


def calculatePerimeterAndAread(usedForCalculation, i, j, regionId, perimeter, area):
    if not indexInMap(i, j):
        return perimeter, area
    if map[i][j]["regionID"] != regionID:
        return perimeter, area
    if usedForCalculation[i][j]:
        return perimeter, area

    usedForCalculation[i][j] = True
    myArea = 1
    myPerimeter = 0
    fenceCount = lambda i, j: 1 if (not indexInMap(i, j) or map[i][j]["regionID"] != regionId) else 0
    myPerimeter += fenceCount(i+1, j)
    myPerimeter += fenceCount(i-1, j)
    myPerimeter += fenceCount(i, j+1)
    myPerimeter += fenceCount(i, j-1)
    perimeterInc = myPerimeter
    areaInc = myArea

    perimeterInc, areaInc = calculatePerimeterAndAread(usedForCalculation, i+1, j, regionID, perimeterInc, areaInc)
    perimeterInc, areaInc = calculatePerimeterAndAread(usedForCalculation, i-1, j, regionID, perimeterInc, areaInc)
    perimeterInc, areaInc = calculatePerimeterAndAread(usedForCalculation, i, j+1, regionID, perimeterInc, areaInc)
    perimeterInc, areaInc = calculatePerimeterAndAread(usedForCalculation, i, j-1, regionID, perimeterInc, areaInc)
    return perimeter + perimeterInc, area + areaInc


price = 0
printMap()

def calculatePerimeterWithNewMethod(regionID):
    sideCount = 0
    for i in range(n):
        prevFence = False
        for j in range(m):
            upDifferent = not indexInMap(i-1, j) or map[i-1][j]["regionID"] != regionID
            thisIsNeededType = map[i][j]["regionID"] == regionID
            nowFence = thisIsNeededType and upDifferent
            if nowFence and not prevFence:
                sideCount += 1
            prevFence = nowFence

    for i in range(n):
        prevFence = False
        for j in range(m):
            downDifferent = not indexInMap(i+1, j) or map[i+1][j]["regionID"] != regionID
            thisIsNeededType = map[i][j]["regionID"] == regionID
            nowFence = thisIsNeededType and downDifferent
            if nowFence and not prevFence:
                sideCount += 1
            prevFence = nowFence

    for j in range(m):
        prevFence = False
        for i in range(n):
            leftDifferent = not indexInMap(i, j-1) or map[i][j-1]["regionID"] != regionID
            thisIsNeededType = map[i][j]["regionID"] == regionID
            nowFence = thisIsNeededType and leftDifferent
            if nowFence and not prevFence:
                sideCount += 1
            prevFence = nowFence

    for j in range(m):
        prevFence = False
        for i in range(n):
            leftDifferent = not indexInMap(i, j+1) or map[i][j+1]["regionID"] != regionID
            thisIsNeededType = map[i][j]["regionID"] == regionID
            nowFence = thisIsNeededType and leftDifferent
            if nowFence and not prevFence:
                sideCount += 1
            prevFence = nowFence

    return sideCount

# 110
# 001011
# 111141

for regionID, location in regionIDLocation.items():
    usedForCalculation = [[False for j in range(m)] for i in range(n)]
    # print("region ID", regionID, "loc", location)
    i = location[0]
    j = location[1]
    per, area = calculatePerimeterAndAread(usedForCalculation, i, j, map[i][j]["regionID"], 0, 0)
    print(map[i][j]["type"], "area", area)
    sides = calculatePerimeterWithNewMethod(map[i][j]["regionID"])
    print("sides", sides)
    price += area*sides

print("answer", price)

