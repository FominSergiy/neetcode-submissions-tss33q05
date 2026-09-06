from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## DFS SOLUTION
        # always take an available node
        # go as deep as possible
        # return once no more edges left
        # n = len(tickets)
        # adj = defaultdict(list)

        # for src, dst in sorted(tickets)[::-1]:
        #     adj[src].append(dst)
        
        # ans = []

        # def dfs(src: str):
        #     while adj[src]:
        #         dst = adj[src].pop()
        #         dfs(dst)
        #     ans.append(src)
        
        # dfs("JFK")
        # return ans[::-1]



        # STACK solution
        n = len(tickets)
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        ans = []
        stack = ['JFK']
        while stack:
            node = stack[-1]
            if adj[node]:
                stack.append(adj[node].pop())
            else:
                ans.append(stack.pop())
        return ans[::-1]
            
