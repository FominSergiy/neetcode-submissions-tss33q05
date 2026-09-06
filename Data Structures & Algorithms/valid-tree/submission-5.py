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
        
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node: int, par: int):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
        




