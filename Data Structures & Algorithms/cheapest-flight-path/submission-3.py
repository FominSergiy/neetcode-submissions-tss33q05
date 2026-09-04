from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        stops = [float("inf")] * n
        stops[src] = 0
        adj = [[] for _ in range(n)]
        for s, d, p in flights:
            adj[s].append((d, p))
        
        heap = [(0, src, 0)] # min based on cost still

        # it works because we check for steps right after we pop
        # this guard is different to previous problem
        # but concept of using helper arr to track weights and heap are the same
        while heap:
            dist, node, steps = heapq.heappop(heap)

            # we have reached the max num of steps
            if steps > k + 1 or steps > stops[node]:
                continue

            # otherwise update the value of current node with current steps
            # we have "just" stepped into it
            stops[node] = steps

            # if reached end, return price
            if node == dst:
                return dist

            # otherwise look at neighbors
            # without any checks since they are done above
            for nei, price in adj[node]:
                heapq.heappush(heap, (price + dist, nei, steps + 1))
        return -1

                
