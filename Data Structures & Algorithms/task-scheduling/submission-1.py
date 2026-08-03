from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1

            if max_heap:
                # task ready for scheduler
                count = -heapq.heappop(max_heap) - 1
                if count > 0:
                    cooldown.append((count, time + n))
            
            if cooldown and cooldown[0][1] == time:
                ready_count, _ = cooldown.popleft()
                heapq.heappush(max_heap, -ready_count)
        
        return time
            