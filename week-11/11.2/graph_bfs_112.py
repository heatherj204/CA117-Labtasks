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
    
class BFSPaths:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False] * g.V
        self.parent = [-1] * g.V
        self.bfs(s)
    
    def bfs(self, s):
        queue = [s]
        self.marked[s] = True
        
        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True
    
    def hasPathTo(self, w):
        return self.marked[w]

    def pathTo(self, w):
        if not self.hasPathTo(w):
            return
        
        path = [w]
        currNode = self.parent[w]
        while currNode != -1:
            path.append(currNode)
            currNode = self.parent[currNode]
            
        return path[::-1]


#test data
#!/usr/bin/env python3
# import sys
# from graph_bfs_112 import Graph, BFSPaths

# def main():

#     with open('graph_input_00_112.txt', 'r') as f:

#         V = int(f.readline().strip())

#         g = Graph(V)

#         for line in f:
#             v, w = [int(t) for t in line.strip().split()]
#             g.addEdge(v, w)

#     bfs = BFSPaths(g, 4)

#     print(bfs.hasPathTo(2))

#     print(bfs.pathTo(2))

# if __name__ == '__main__':
#     main()