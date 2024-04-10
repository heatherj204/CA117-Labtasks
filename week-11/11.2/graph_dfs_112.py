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

class DFSPaths(object):

    def __init__(self, g, s) -> None:
        self.g = g
        self.s = s
        # creaste a list to record where we have been so far
        # initially we have not been anywhere
        self.visited = [False] * g.V
        # create a list to recods how we got to each vertext
        # i.e its parent
        self.parent = [-1] * g.V
        self.dfs(s)

    def dfs(self, v):
        #we are at  vertex v so we have not visited it
        # mark it as visited
        self.visited[v] = True
        #where can we go from vertex v?
        for w in self.g.adj[v]:
            # consider going to w
            # only go if it is not already visited
            if not self.visited[w]:
                #before we go there, record where we are coming form
                self.parent[w] = v
                # contiue searching from w
                self.dfs(w)

    def hasPathTo(self, v):
        # is v reachable from our stating point?
        return self.visited[v]

    # return th epath from s to v
    def pathTo(self, v):
        # if there is no path to v
        if not self.hasPathTo(v):
            return []
        path = [v]
        #while not back at the start
        while v != self.s:
            v = self.parent[v]
            path.append(v)

        #we have constructed v ---> s
        #we want to return s ----> v
        return path[::-1] # reverse the list
#test data
#!/usr/bin/env python3
import sys
from graph_dfs_112 import Graph, DFSPaths
def main():
    with open('graph_input_00_112.txt', 'r') as f:
        V = int(f.readline().strip())
        g = Graph(V)
        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)
    dfs = DFSPaths(g, 4)
    print(dfs.hasPathTo(2))
    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()