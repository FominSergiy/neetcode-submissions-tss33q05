from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return len
        # EDGES HAVE DIRECTION!
        # indegree count but make it pre-req -> course
        # to build correct output
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        output = []
        while q:
            crs = q.popleft()
            output.append(crs)

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return output if len(output) == numCourses else []
        