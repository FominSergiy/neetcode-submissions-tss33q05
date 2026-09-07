from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # two approaches - dfs while building adj graph
        # if visited similar node, the this is the one we need to output
        # it works because we traverse adj graph left to right
        # there is 1 extra edge - which means that, once we have encoutered it
        # the next time we see it in see IS the one we need to return
        # track seen within the loop of adj graph
        n = len(edges)
        adj = [[] for _ in range(n)]

        def dfs(node: int, par: int):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

            visited = set()
            if dfs(u - 1, -1):
                return [u, v]


        
        # kahn's idea of peeling indegrees with 1 until no left
        # return last one from right with indegree == 2

        # after peeling of branches with 1 edge are done
        # indregrees are only left with nodes ON the cycle - therefore, we check for both
        # both should have indegree == 2
        
