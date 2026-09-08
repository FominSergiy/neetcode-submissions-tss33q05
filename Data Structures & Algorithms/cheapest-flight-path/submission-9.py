from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # still track elements in heap based on price
        # but use stops as weights
        # before stepping into adj nodes, check for stops
        stops = [float("inf")] * n
        stops[src] = 0
        adj = [[] for _ in range(n)]

        for s, d, p in flights:
            adj[s].append((d, p))
        
        heap = [(0, src, 0)] # cost, node, stops
        while heap:
            cost, node, step = heapq.heappop(heap)

            # overshot in terms of stops
            if step > k + 1 or step > stops[node]:
                continue
            
            if node == dst:
                return cost
            
            # set stops for current node at step
            # otherwsie never ending loop since we dont update the state as we traverse
            stops[node] = step
            # otherwise add to heap
            for nei, cost_to in adj[node]:
                heapq.heappush(heap, (cost_to + cost, nei, step + 1))
        return -1