from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def detect(self , v, visited , stack):
        visited[v]=True
        stack[v]=True
        for neighbour in self.graph[v]:
            if visited[neighbour]==False:
                if self.detect(neighbour , visited , stack)==True:
                    return True
                elif stack[neighbour]==True:
                    return True
        stack[v]=False
        return False

    def isCyclic(self):
        visited = False *[self.V]
        stack = False *[self.V]
        for i in range(self.V):
            if visited[i]==False:
                if self.detect(i , visited , stack) == True:
                    return True
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")

