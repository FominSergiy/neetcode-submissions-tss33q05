from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TOPOLOGICAL SORT
        # indegree = [0] * numCourses
        # adj = [[] for _ in range(numCourses)]

        # for crs, pre in prerequisites:
        #     indegree[pre] += 1
        #     adj[crs].append(pre)
        
        # q = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)
        
        # taken = 0
        # while q:
        #     crs = q.popleft()
        #     taken += 1

        #     for pre in adj[crs]:
        #         indegree[pre] -= 1
        #         if indegree[pre] == 0:
        #             q.append(pre)
        
        # return taken == numCourses

        # DFS approach
        # build the adj map and go backward starting from the 1st course
        # and iterate over EACH course with dfs
        # dfs tries to go back and reach a point where node has no pre-req
        # because we set pre_req to empty to each node we traverse back, it is relatively fast
        adj = [[] for _ in range(numCourses)]
        for src, pre in prerequisites:
            adj[src].append(pre)

        visited = set()

        def dfs(node: int):
            if node in visited:
                return False
            if adj[node] == []:
                return True
            
            visited.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            
            visited.remove(node)
            adj[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

