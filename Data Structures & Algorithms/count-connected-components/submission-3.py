class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # need to connect components and make adj list of all the edges
        # track visited
        visited = set()
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node: int) -> bool:
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt