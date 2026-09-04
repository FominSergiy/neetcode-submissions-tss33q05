from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # two approaches - dfs while building adj graph
        # if visited similar node, the this is the one we need to output
        # it works because we traverse adj graph left to right
        # there is 1 extra edge - which means that, once we have encoutered it
        # the next time we see it in see IS the one we need to return
        # track seen within the loop of adj graph
        # n = len(edges)
        # adj = [[] for _ in range(n + 1)] #offset starting for 0

        # # finding cycles
        # def dfs(node: int, par: int):
        #     if node in visited:
        #         return True
            
        #     visited.add(node)
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False
        
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visited = set()

        #     if dfs(u, -1):
        #         return [u, v]
        
        # kahn's idea of peeling indegrees with 1 until no left
        # return last one from right with indegree == 2
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[v].append(u)
            adj[u].append(v)
        
        queue = deque()
        for i in range(n + 1):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            indegree[node] -= 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
        # after peeling of branches with 1 edge are done
        # indregrees are only left with nodes ON the cycle - therefore, we check for both
        # both should have indegree == 2
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v] == 2:
                return [u, v]
        return []
        
