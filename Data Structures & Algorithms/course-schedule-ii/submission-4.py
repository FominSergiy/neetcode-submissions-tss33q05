from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return len
        # EDGES HAVE DIRECTION!
        # indegree count but make it pre-req -> course
        # to build correct output
        n = numCourses
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for crs, pre in prerequisites:
            indegree[crs] += 1 # courses has + 1 pre-req
            adj[pre].append(crs)
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        output = []
        while queue:
            node = queue.popleft()
            output.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return output if len(output) == n else []
        