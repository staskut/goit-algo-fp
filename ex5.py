import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import colorsys


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, tree_node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree_node_colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, with_labels=True)
    plt.axis('off')
    plt.show()


def dfs(node, tree_node_colors, tree_color_index, tree_total_nodes):
    """
    Depth-first search function to color tree nodes based on a given color index and total nodes count.
    Args:
        node: The current node in the tree.
        tree_node_colors: A dictionary to store the color of each tree node.
        tree_color_index: The index of the current color in the color sequence.
        tree_total_nodes: Total number of nodes in the tree.
    Returns:
        Updated tree_color_index after processing the entire tree.
    """
    if node:
        node.color = get_rgb_color(tree_color_index, tree_total_nodes)
        tree_node_colors[node.id] = node.color
        tree_color_index += 1

        tree_color_index = dfs(node.left, tree_node_colors, tree_color_index, tree_total_nodes)
        tree_color_index = dfs(node.right, tree_node_colors, tree_color_index, tree_total_nodes)

    return tree_color_index


def bfs(node, tree_node_colors, tree_color_index, tree_total_nodes):
    """
    Perform a breadth-first search on a tree to assign colors to its nodes
    Parameters:
    - node: the starting node for the search
    - tree_node_colors: a dictionary to store the colors of tree nodes
    - tree_color_index: the index of the color to be assigned to the nodes
    - tree_total_nodes: the total number of nodes in the tree
    Returns:
    - The updated index of the color to be assigned to the nodes
    """
    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        current_node.color = get_rgb_color(tree_color_index, tree_total_nodes)
        tree_node_colors[current_node.id] = current_node.color
        tree_color_index += 1

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return tree_color_index


def get_rgb_color(index, total_colors):
    """
    Calculate and return an RGB color based on the index and total number of colors provided.
    Parameters:
    index (int): The index of the color to calculate.
    total_colors (int): The total number of colors available.
    Returns:
    str: The RGB color code in the format "#RRGGBB".
    """
    s = float(index) / float(total_colors)
    rgb = colorsys.hsv_to_rgb(1.0, s, 1.0)
    color = "#{:02x}{:02x}{:02x}".format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)).replace("-", "")
    return color


# Створення дерева
root = Node(10)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
root.left.left.left = Node(7)
root.left.left.right = Node(6)

total_nodes = root.val
color_index = 1

# Обхід дерева в глибину
node_colors = {}
color_index = dfs(root, node_colors, color_index, total_nodes)
draw_tree(root, node_colors)

# Обхід дерева в ширину
node_colors = {}
color_index = bfs(root, node_colors, color_index, total_nodes)
draw_tree(root, node_colors)
