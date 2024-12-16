import heapq

def dijkstra(graph, start):
    # graph - представление графа в виде словаря {узел: [(сосед, вес), ...]}
    # start - начальная вершина
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (вес, узел)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('C', 2), ('D', 5)],
#     'C': [('D', 1)],
#     'D': []
# }

# start_node = 'A'
# shortest_paths = dijkstra(graph, start_node)

# print(shortest_paths)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}


def solve(input):
    data = open(input, "r+t").readlines()
    data = data[1:len(data)-1]
    data = [line[1:len(line)-2] for line in data]

    h = len(data)
    w = len(data[0])

    # print(h, w)

    graph = {}

    in_map = lambda x, y: 0 <= x < w and 0 <= y < h and data[y][x] != '#'

    pos = lambda x, y, d: f"{x}_{y}_{d}"

    for y in range(h):
        for x in range(0, w):
            if data[y][x] == '#':
                continue

            ea = pos(x, y, 'e')
            we = pos(x, y, 'w')
            no = pos(x, y, 'n')
            so = pos(x, y, 's')

            graph[ea] = []
            graph[we] = []
            graph[no] = []
            graph[so] = []

            graph[we].append((no, 1000))
            graph[we].append((so, 1000))
            graph[ea].append((no, 1000))
            graph[ea].append((so, 1000))
            graph[no].append((we, 1000))
            graph[no].append((ea, 1000))
            graph[so].append((we, 1000))
            graph[so].append((ea, 1000))

            if in_map(x+1,y):
                ea_nb = pos(x+1, y, 'e')
                graph[ea].append((ea_nb, 1))

            if in_map(x-1,y):
                we_nb = pos(x-1, y, 'w')
                graph[we].append((we_nb, 1))

            if in_map(x,y-1):
                no_nb = pos(x, y-1, 'n')
                graph[no].append((no_nb, 1))

            if in_map(x,y+1):
                so_nb = pos(x, y+1, 's')
                graph[so].append((so_nb, 1))

    start_node = pos(0, h-1, 'e')
    shortest_paths = dijkstra(graph, start_node)

    y = 0
    x = w - 1
    a = shortest_paths[pos(x, y, 'e')]
    b = shortest_paths[pos(x, y, 'w')]
    c = shortest_paths[pos(x, y, 'n')]
    d = shortest_paths[pos(x, y, 's')]
    print(min(a, b, c, d))

import sys
solve(sys.argv[1])

