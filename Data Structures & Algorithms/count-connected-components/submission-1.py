class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # adj graph for all nodes
        # just dfs into each component
        # after dfs increment component count += 1
        def dfs(node: int):
            stack = [node]
            while stack:
                n = stack.pop()

                for nei in adj[n]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            
            return
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        
        return count