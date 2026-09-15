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
        
        # build adj list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def has_cycle(node: int, parent: int) -> bool:
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if has_cycle(nei, node):
                    return True
            return False
        
        return not has_cycle(0, -1) and len(visited) == n
            
        
            



