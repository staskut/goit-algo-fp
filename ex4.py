import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="lightgreen"):  # Змінив колір для наглядності максимальної купи
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, left_x, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, right_x, y - 1, layer + 1)

def draw_heap(tree_root):
    heap_graph = nx.DiGraph()
    positions = {tree_root.id: (0, 0)}
    add_edges(heap_graph, tree_root, positions)

    node_colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    node_labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=positions, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Створення максимальної бінарної купи як приклад
root = Node(10)  # Корінь має найбільше значення
root.left = Node(8)
root.right = Node(9)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(2)
root.right.right = Node(5)

# Візуалізація купи
draw_heap(root)
