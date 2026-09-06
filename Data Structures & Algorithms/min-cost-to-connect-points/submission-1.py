class DSU:
    def __init__(self, n: int):
        # why n + 1?
        self.parent = list(range(n))
        self.size = [0] * n
    
    def find(self, node: int):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False # already connected
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.parent[pv] = self.parent[pu]
        self.size[pu] += self.size[pv]
        return True
 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        # list of edges
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        ans = 0
        # iterate over sorted edges, if set connect, add cost
        # sort to get min distance
        edges.sort()
        for dist, u, v in edges:
            if dsu.union(u, v):
                ans += dist
        return ans
