from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegrees = {c: 0 for c in adj }


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # for any word where a > b and they have same chars at min len
            # such ordering is not valid - exit early
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # otherwise look for a word mismatch - that creates an edge between the two
            # only add it once since we also increment indegree
            # and set indegree of w2 char to += 1 -> we jus created an edge w1 > w2
            # therefore w2 has +1 indegree
            # directed edge from w1 -> w2 because they supposed to be sorted in asc already
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegrees[w2[j]] += 1
                    break

        queue = deque()

        for char in indegrees:
            if indegrees[char] == 0:
                queue.append(char)
        
        ans = []
        while queue:
            char = queue.popleft()
            ans.append(char)

            for nei_char in adj[char]:
                indegrees[nei_char] -= 1
                if indegrees[nei_char] == 0:
                    queue.append(nei_char)
        
        return "".join(ans) if len(ans) == len(indegrees) else ""

                

        