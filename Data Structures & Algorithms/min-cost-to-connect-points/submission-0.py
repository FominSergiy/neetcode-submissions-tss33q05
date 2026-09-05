class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        # make pv main of size pu < pv
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        # union the two
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = [] # (distance, node)

        for i in range(n):
            for j in range(i + 1, n):
                dist = self.get_dist(points[i], points[j])
                edges.append((dist, i, j))
        
        edges.sort() # sort in asc order based on distance
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res

    def get_dist(self, point1: list[int], point2: list[int]) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        