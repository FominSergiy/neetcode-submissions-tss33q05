from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree is one that
        # 1. has no cycles
        # 2. all nodes are reachable

        # since we have undirected edges
        # we make a by-directional list and dfs from 0 node
        # we we encounter visited node -> cycle
        # otherwise keep traversing
        if len(edges) > n:
            return False
        
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # indentify cycle
        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        ans = dfs(0, -1)
        return not ans and len(visited) == n
        
            



