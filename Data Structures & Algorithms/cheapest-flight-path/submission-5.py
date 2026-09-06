from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # still track elements in heap based on price
        # but use stops as weights
        # before stepping into adj nodes, check for stops
        stops = [float('inf')] * n
        stops[src] = 0
        adj = [[] for _ in range(n)]

        for u, v, p in flights:
            adj[u].append((v, p))
        
        heap = [(0, src, 0)]
        while heap:
            price, node, steps = heapq.heappop(heap)
            
            # took too many steps - this path invalid
            if steps > k + 1 or steps > stops[node]:
                continue
            
            # if reached dest, return price
            if node == dst:
                return price

            # otherwise explore nei
            stops[node] = steps
            for nei, price_to_nei in adj[node]:
                heapq.heappush(heap, (price_to_nei + price, nei, steps + 1))
        return -1
                
