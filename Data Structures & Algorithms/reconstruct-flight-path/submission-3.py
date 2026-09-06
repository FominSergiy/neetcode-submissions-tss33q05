from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## DFS SOLUTION
        # always take an available node
        # go as deep as possible
        # return once no more edges left
        n = len(tickets)
        adj = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        ans = []

        def dfs(src: str):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            ans.append(src)
        
        dfs("JFK")
        return ans[::-1]



        # STACK solution
        # n = len(tickets)
        # adj = defaultdict(list)
        # for src, dst in sorted(tickets)[::-1]:
        #     adj[src].append(dst)
        
        # ans = []
        # stack = ['JFK']
        # # check top of stack
        # # if no more adj, add to ans
        # # else add adj to stack
        # while stack:
        #     node = stack[-1]
        #     if not adj[node]:
        #         ans.append(stack.pop())
        #     else:
        #         stack.append(adj[node].pop())
        # return ans[::-1]
            

            
