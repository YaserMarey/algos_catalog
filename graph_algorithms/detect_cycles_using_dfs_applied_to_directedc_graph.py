# Detecting cycles in directed graphs using DFS
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    # The function to do DFS traversal. It uses recursive explore
    def DFS(self):
        # Mark all the vertices as not visited
        visited = {}
        stack = {}
        for v in self.graph:
            visited[v] = False
            stack[v] = False
            for u in self.graph[v]:
                visited[u] = False
                stack[v] = False

        # Explore every node
        for v in self.graph.copy():
            if not visited[v]:
                if self.explore_if_cycles_exist(v, visited, stack):
                    print('Graph has a cycle!')
                    return True
        print('Graph doesn\'t have a cycle')
        return False

    def explore_if_cycles_exist(self, v, visited, stack):
        # Mark the current node as visited and print it
        visited[v] = True
        stack[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                if self.explore_if_cycles_exist(i, visited, stack):
                    return True
            elif stack[v]:
                    return True
        stack[v] = False
        return False


def main():
    g = Graph(1)
    g.addedge('A', 'A')
    g.DFS()

    g = Graph(3)
    g.addedge('B', 'C');
    g.addedge('C', 'A');
    g.addedge('A', 'B');
    g.DFS()

    g = Graph(4)
    g.addedge('A', 'D');
    g.addedge('D', 'E');
    g.addedge('D', 'G');
    g.DFS()
#
#
if __name__ == '__main__':
    main()
