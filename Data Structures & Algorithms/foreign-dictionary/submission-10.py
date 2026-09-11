from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        n = len(words)
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            l1, l2 = len(w1), len(w2)
            min_len = min(l1, l2)

            if l1 > l2 and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
            
        output = []
        while queue:
            char = queue.popleft()
            output.append(char)

            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return "".join(output) if len(output) == len(indegree) else ""