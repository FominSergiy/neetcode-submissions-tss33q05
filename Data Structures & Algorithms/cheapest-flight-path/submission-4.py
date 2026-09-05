from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        stops = [float("inf")] * n
        stops[src] = 0
        adj = [[] for _ in range(n)]
        for s, d, p in flights:
            adj[s].append((d, p))
        
        # min heap by price to get smallest price with o(1)
        heap = [(0, src, 0)]
        while heap:
            price_so_far, node, steps = heapq.heappop(heap)

            # too many steps
            if steps > stops[node] or steps > k + 1:
                continue
            
            # check if reached destination
            if node == dst:
                return price_so_far
            
            # since we do the checks above, at this step we can safely add to the heap
            stops[node] = steps
            for nei, price in adj[node]:
                heapq.heappush(heap, (price_so_far + price, nei, steps + 1))
        return -1
            

                
