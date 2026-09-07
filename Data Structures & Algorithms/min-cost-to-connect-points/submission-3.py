class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n # track the size of component at index i
    
    def find(self, node: int):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)

        # already part of the same parent
        if pu == pv:
            return False
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        # print(self.size)
        self.parent[pv] = self.parent[pu]
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
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        # since we need smallest, sort edges in asc order
        # so that we work with edges that have smallest distance in-between
        # dsu is used to check if edges are already part of the same object
        # and that is done given the edges
        # dsu looks up to the parent and uses path compression to make
        # the check effecient
        ans = 0
        # iterate over sorted edges, if set connect, add cost
        # sort to get min distance
        edges.sort()
        for dist, u, v in edges:
            if dsu.union(u, v):
                ans += dist
        return ans
