import heapq


def dijkstra(weighted_graph, start_vertex):
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху в графі.
    Args:
        weighted_graph: словник, що представляє зважений граф, де ключі - це вершини, а значення - це словники
         сусідів і ваг
        start_vertex: початкова вершина для алгоритму
    Returns:
        shortest_distances: словник, що містить найкоротші відстані від початкової вершини до всіх інших вершин
    """

    shortest_distances = {vertex: float('infinity') for vertex in weighted_graph}
    shortest_distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        distance_to_current_vertex, current_node = heapq.heappop(priority_queue)

        if distance_to_current_vertex > shortest_distances[current_node]:
            continue

        for adjacent_node, edge_weight in weighted_graph[current_node].items():
            distance = distance_to_current_vertex + edge_weight
            if distance < shortest_distances[adjacent_node]:
                shortest_distances[adjacent_node] = distance
                heapq.heappush(priority_queue, (distance, adjacent_node))

    return shortest_distances


test_graph = {
    'A': {'B': 7, 'C': 8},
    'B': {'A': 11, 'C': 2, 'D': 5},
    'C': {'A': 7, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 2}
}
start_vertex = 'A'

shortest_distances = dijkstra(test_graph, start_vertex)

for destination, distance in shortest_distances.items():
    print(f"Найкоротша відстань від {start_vertex} до {destination}: {distance}")

# Найкоротша відстань від A до A: 0
# Найкоротша відстань від A до B: 7
# Найкоротша відстань від A до C: 8
# Найкоротша відстань від A до D: 9

start_vertex = 'C'

shortest_distances = dijkstra(test_graph, start_vertex)

for destination, distance in shortest_distances.items():
    print(f"Найкоротша відстань від {start_vertex} до {destination}: {distance}")

# Найкоротша відстань від C до A: 7
# Найкоротша відстань від C до B: 2
# Найкоротша відстань від C до C: 0
# Найкоротша відстань від C до D: 1
