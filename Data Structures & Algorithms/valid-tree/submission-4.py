from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree is one that
        # 1. has no cycles
        # 2. all nodes are reachable

        if len(edges) > n:
            return False
        
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # by dfs from 0 node, we iterate down
        # if we have cycle other than parents - False
        # else we add to visited
        # at the end size should equal n - all nodes are connected
        q = deque([(0, -1)])
        visited = set()
        visited.add(0)
        while q:
            node, parent = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                else:
                    visited.add(nei)
                    q.append((nei, node))
    
        return len(visited) == n



