from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS solution with sorting

        # TOPOLOGICAL SORT
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0
        while q:
            crs = q.popleft()
            taken += 1

            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return taken == numCourses

