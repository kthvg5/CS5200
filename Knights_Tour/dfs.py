# Don't use odd libraries
# Open tour gets partial credit
# Not testing anything bigger than 8x8


import sys
import copy
import stack


class Node(object):
    def __init__(self, neighbors, used):
        self.neighbors = neighbors
        self.used = used


def dfs(graph, path):
    parent = path.top()
#    print "parent = ", parent
    moves = graph[parent].neighbors

    if path.size() == len(graph):
        if path.data[0] in moves:
            print "found one!"
            return True
        else:
            return False
    else:
        for move in moves:
            if graph[move].used is False:
                graph[move].used = True
                path.push(move)
                if dfs(graph, path):
                    return True
                else:
                    graph[move].used = False
                    path.pop()


def main():
    n = int(sys.argv[1])
    moves = [(2, -1), (2, 1), (1, 2), (-1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1)]
    graph = dict()
    node_moves = set()
    path = stack.Stack()
    for i in range(0, n):
        for j in range(0, n):
            for move in moves:
                if 0 <= i + move[0] < n and 0 <= j + move[1] < n:
                    node_moves.add((i + move[0], j + move[1]))
            graph[(i, j)] = (Node(copy.deepcopy(node_moves), False))
            node_moves = set()
    graph[(n/2, n/2)].used = True
    path.push((n/2, n/2))
    dfs(graph, path)
    path.print_stack()


if __name__ == "__main__":
    main()
