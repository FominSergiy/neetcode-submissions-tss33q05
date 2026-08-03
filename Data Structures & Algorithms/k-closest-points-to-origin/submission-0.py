from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [(abs(x**2 + y**2), (x, y)) for x,y in points]
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            item = heapq.heappop(heap)
            ans.append(item[1])
        
        return ans

