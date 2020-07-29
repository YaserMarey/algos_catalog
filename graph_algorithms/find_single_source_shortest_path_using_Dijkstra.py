# find single source shortest path in directed graph using Bellman-Ford algorithm
# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

        # The main function that finds shortest distances from src to

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for i in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for u, v, w in self.graph:
                if not sptSet[v] and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.printSolution(dist)

        # A utility function to find the vertex with
        # minimum distance value, from the set of vertices
        # not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = -float("Inf")

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
# g.BellmanFord(0)
g.dijkstra(0)
