# Finding vertices topological order by applying in directed graph using Depth First Search
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.stack = [0] * 2 * n
        self.order = 0

    def addedge(self, u, v):
        self.graph[u].append(v)

    # The function to do DFS traversal. It uses recursive explore
    def DFS(self):
        # Mark all the vertices as not visited
        visited = {}
        for v in self.graph:
            visited[v] = False
            for u in self.graph[v]:
                visited[u] = False
        # Explore every node
        for v in self.graph.copy():
            if not visited[v]:
                self.explore(v, visited)
        print(self.stack)

    def explore(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        self.order += 1
        for i in self.graph[v]:
            if not visited[i]:
                self.explore(i, visited)
        self.stack[self.order] = v
        self.order += 1


def main():
    g = Graph(8)
    g.addedge('B', 'A')
    g.addedge('B', 'C')
    g.addedge('F', 'B')
    g.addedge('B', 'E')
    g.addedge('A', 'D')
    g.addedge('D', 'E')
    g.addedge('D', 'G')
    g.addedge('E', 'G')
    g.addedge('H', 'G')
    g.addedge('F', 'H')

    g.DFS()


if __name__ == '__main__':
    main()
