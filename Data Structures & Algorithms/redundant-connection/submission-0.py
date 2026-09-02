class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # two approaches - dfs while building adj graph
        # if visited similar node, the this is the one we need to output
        # it works because we traverse adj graph left to right
        # there is 1 extra edge - which means that, once we have encoutered it
        # the next time we see it in see IS the one we need to return
        # track seen within the loop of adj graph
        n = len(edges)
        adj = [[] for _ in range(n + 1)] #offset starting for 0

        # finding cycles
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
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if dfs(u, -1):
                return [u, v]
