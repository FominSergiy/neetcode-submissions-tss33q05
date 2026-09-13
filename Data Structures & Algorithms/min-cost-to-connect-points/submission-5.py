class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node: int):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.parent[pv] = self.parent[pu]
        self.size[pu] += self.size[pv]
        return True
 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # we can do the connection by using DSU
        # which allows us to check if two points are already connected
        # and if not, we get the min cost of connecting the two
        n = len(points)
        dsu = DSU(n)


        # build list of edges of every point with one another
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i, j))
    
        # since we need smallest, sort edges in asc order
        # so that we work with edges that have smallest distance in-between
        # dsu is used to check if edges are already part of the same object
        # and that is done given the edges
        # dsu looks up to the parent and uses path compression to make
        # the check effecient
        # iterate over sorted edges, if set connect, add cost
        # sort to get min distance
 
        edges.sort()
        min_cost = 0
        for cost, u, v in edges:
            if dsu.union(u, v):
                min_cost += cost
        
        return min_cost

