from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # pre-build for missing ones
        # pre_map = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     pre_map[crs].append(pre)
        
        # needs to be kept for a current path, not globally
        # almost like backtrack
        # visiting = set()

        # def dfs(crs: int) -> bool:
        #     if crs in visiting:
        #         return False # cycle
        #     # else we arrived at crs with no pre-req -base case, return
        #     if pre_map[crs] == []:
        #         return True
            
        #     # we look at this course's pre-req and try again
        #     visiting.add(crs)
        #     for pre in pre_map[crs]:
        #         if not dfs(pre):
        #             return False
        #     # at this point we know we can reach back
        #     visiting.remove(crs)
        #     # clear all pre-reqs for this course, tested with the above, we are good
        #     pre_map[crs] = []
        #     return True


        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True

        # TOPO SORT (KAHN'S ALGO)
        in_degree = [0] * numCourses
        adjacent = [[] for _ in range(numCourses)]

        # bulld in_degrees and adjacent
        for src, dst in prerequisites:
            in_degree[dst] += 1
            adjacent[src].append(dst)
        
        finished = 0
        q = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i) # add course to queue

        while q:
            node = q.popleft()
            finished += 1
            
            for pre in adjacent[node]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    q.append(pre)
        
        return finished == numCourses

