# python3

import sys
import threading


class Node:
    def __init__(self, value=None):
        self._value = value
        self._childrens = []

    def add_children(self, children):
        self._childrens.append(children)

    def get_childrens(self):
        return self._childrens

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


def DFS_recursive(root, depth):
    childrens_depths = []
    if len(root.get_childrens()) == 0:
        return depth

    for children in root.get_childrens():
        #        print(f"children value: {children.get_value()}")
        #        print(f"childrens len: {len(children.get_childrens())}")
        childrens_depths.append(DFS_recursive(children, depth + 1))

#    print(childrens_depths)
    return (max(childrens_depths))


def compute_height(n, parents):
    tree = []

    for i, node in enumerate(parents):
        tree.append(Node(i))
        if node == -1:
            root_index = i

    for i, node in enumerate(parents):

        if node == -1:
            continue

        tree[node].add_children(tree[i])

    return DFS_recursive(tree[root_index], 0) + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
