from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        finish, output = 0, []
        while q:
            node = q.popleft()
            finish += 1
            output.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return output if finish == numCourses else []