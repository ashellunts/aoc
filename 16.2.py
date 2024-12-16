import heapq

def dijkstra(graph, start):
    global best_paths_tiles_count

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

pos = lambda x, y, d: f"{x}_{y}_{d}"


def search_all_paths(go_to, best_paths_tiles_count, graph, shortest_paths):

    tile = go_to[:len(go_to)-2]
    best_paths_tiles_count[tile] = True

    start_node = pos(0, h-1, 'e')
    if start_node == go_to:
        return

    from_where_can_i_reach_go_to = []
    for v, nbs in graph.items():
        for nb in nbs:
            if nb[0] == go_to:
                from_where_can_i_reach_go_to.append(v)

    shortest_path_to_go_to = shortest_paths[go_to]

    for nb in from_where_can_i_reach_go_to:
        shortest_path_to_nb = shortest_paths[nb]
        path_from_nb_to_go_to = next(filter(lambda neighbor: neighbor[0] == go_to, graph[nb]))

        if shortest_path_to_go_to == shortest_path_to_nb + path_from_nb_to_go_to[1]:
            # print('goto ', path_from_nb_to_go_to[0])
            search_all_paths(nb, best_paths_tiles_count, graph, shortest_paths)



import sys
input = sys.argv[1]


data = open(input, "r+t").readlines()
data = data[1:len(data)-1]
data = [line[1:len(line)-2] for line in data]

h = len(data)
w = len(data[0])

graph = {}

in_map = lambda x, y: 0 <= x < w and 0 <= y < h and data[y][x] != '#'

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
res = min(a, b, c, d)
print(res)

y = 0
x = w -1

best_paths_tiles_count = {
}

end_node=pos(x, y, 'e')
if shortest_paths[end_node] == res:
    search_all_paths(end_node, best_paths_tiles_count, graph, shortest_paths)

end_node=pos(x, y, 'n')
if shortest_paths[end_node] == res:
    search_all_paths(end_node, best_paths_tiles_count, graph, shortest_paths)

print(len(best_paths_tiles_count))
