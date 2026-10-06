from collections import Counter, deque
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap to store freq of tasks
        counter = Counter(tasks)
        heap = [-cnt for cnt in counter.values()]
        heapq.heapify(heap)
        queue = deque() # (frequency, time)

        time = 0
        while heap or queue:
            time += 1

            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap) # negative nums therefore + 1
                if cnt:
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
            
                

            