from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dls(self,source,target,maxDepth):
        if source == target: return True
        if maxDepth<= 0: return False
        for i in self.graph[source]:
            if (self.dls(i,target,maxDepth-1)):
                return True
        return False
g = graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(3,8)
target = 3
maxDepth= 3
source = 0
if g.dls(source,target,maxDepth)==True:
    print(f"target {target} is reachable from source {source} within maximum depth {maxDepth}")
else:
    print(f"target{target}is not reachable from source {source} within maximum depth{maxDepth}")

