from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        # use specifically because we dfs into des
        # and otherwise we have to build adj graph for src, dst, at least
        # for them to have keys
        adj = defaultdict(list)

        # build in reverse
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(node: int):
            while adj[node]:
                dest = adj[node].pop()
                dfs(dest)
            res.append(node)

        dfs("JFK")
        # since ans was build in treverse, we need to reverse it back to
        # get the right order
        return res[::-1]

            
