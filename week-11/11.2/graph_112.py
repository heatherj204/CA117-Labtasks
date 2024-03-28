class Graph(object):
    def __init__(self, V) -> None:
        self.V = V
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        self.adj[v]
        return len(self.adj[v])

    def degreelistfun(self):
        degreelst = []
        for v in range(self.V):
            degreelst.append(self.degree(v))
        return degreelst

    def maxDegree(self):
        degreelist = self.degreelistfun()
        return max(degreelist)

    def avgDegree(self):
        degreelist = self.degreelistfun()
        total = 0
        for i in degreelist:
            total += i
        average = total / len(degreelist)
        return average

#test data
#!/usr/bin/env python3
# import sys
# from graph_112 import Graph
# def main():
#     with open('graph_input_00_112.txt', 'r') as f:
#         V = int(f.readline().strip())
#         g = Graph(V)
#         for line in f:
#             v, w = [int(t) for t in line.strip().split()]
#             g.addEdge(v, w)
#     for v in range(g.V):
#         print('Vertex {} connects to {}'.format(v, g.adj[v]))
#     for v in range(V):
#         print('Degree of vertex {} is {}'.format(v, g.degree(v)))
#     print('Maximum degree is {}'.format(g.maxDegree()))
#     print('Average degree is {:.2f}'.format(g.avgDegree()))

# if __name__ == '__main__':
#     main()