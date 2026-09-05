from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## DFS SOLUTION
        # n = len(tickets)
        # # use specifically because we dfs into des
        # # and otherwise we have to build adj graph for src, dst, at least
        # # for them to have keys
        # adj = defaultdict(list)

        # # build in reverse
        # for src, dst in sorted(tickets)[::-1]:
        #     adj[src].append(dst)

        # res = []
        # def dfs(node: int):
        #     while adj[node]:
        #         dest = adj[node].pop()
        #         dfs(dest)
        #     res.append(node)

        # dfs("JFK")
        # # since ans was build in treverse, we need to reverse it back to
        # # get the right order
        # return res[::-1]

        # STACK solution
        n = len(tickets)
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        ans = []
        stack = ['JFK']
        # check top of stack
        # if no more adj, add to ans
        # else add adj to stack
        while stack:
            node = stack[-1]
            if not adj[node]:
                ans.append(stack.pop())
            else:
                stack.append(adj[node].pop())
        return ans[::-1]
            

            
