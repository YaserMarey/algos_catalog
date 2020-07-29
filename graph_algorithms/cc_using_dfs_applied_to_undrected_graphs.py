# Finding connected components in undirected graph using Depth First Search
from collections import defaultdict


class GraphUndirected:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        # Here we add two edges in both direction to simulate undirected edges
        self.graph[u].append(v)  # undirected
        self.graph[v].append(u)  # undirected

    # The function to do DFS traversal. It uses recursive explore

def DFS(G):
    # Mark all the vertices as not visited
    cc = 0
    visited = [False] * (len(G.graph))
    # Explore every node
    for v in G.graph:
        if not visited[v]:
            cc += 1
            explore(G, v, visited, cc)

def explore(G, v, visited, cc):
    # Mark the current node as visited and print it
    visited[v] = True
    print('{0} cc={1}'.format(v, cc))
    # Recur for all the vertices adjacent to this vertex
    for i in G.graph[v]:
        if not visited[i]:
            explore(G, i, visited, cc)

def main():
    g = GraphUndirected()
    g.addedge(0, 1)
    g.addedge(0, 2)
    g.addedge(3, 4)

    DFS(g)


if __name__ == '__main__':
    main()
