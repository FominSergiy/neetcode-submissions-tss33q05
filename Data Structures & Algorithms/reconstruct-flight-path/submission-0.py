from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        # use specifically because we dfs into des
        # and otherwise we have to build adj graph for src, dst, at least
        # for them to have keys
        adj = defaultdict(list)

        # build in reverse
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []
        def dfs(node: int):
            while adj[node]:
                dest = adj[node].pop()
                dfs(dest)
            res.append(node)

        dfs("JFK")
        return res[::-1]

            
