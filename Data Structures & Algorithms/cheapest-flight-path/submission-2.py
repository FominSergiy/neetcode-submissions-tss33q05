from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        stops = [float('inf')] * n
        graph = [[] for _ in range(n)]
        for x, y, p in flights:
            graph[x].append((p, y)) # price (weight) + destination

        heap = [(0, src, 0)]
        while heap:
            price_so_far, node, steps = heapq.heappop(heap)

            # we have reached the max num of steps
            if steps > stops[node] or steps > k + 1:
                continue
            
            # check if at destination
            # print(node)
            # print(graph[node])
            stops[node] = steps
            if node == dst:
                return price_so_far
            
            for price, nei in graph[node]:
                heapq.heappush(heap, (price_so_far + price, nei, steps + 1))

        return -1
    