from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node: int, parent:int):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            return True
        
        visited = set()
        return dfs(0, -1) and len(visited) == n



