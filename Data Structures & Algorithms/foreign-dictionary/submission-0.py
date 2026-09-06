class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # that means w1 is NOT a prefix and it has more chars than w2
            # therefore, it is impossible based on the rule 2
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # for 2 adj words, 1st position where words differ tells us about the order
            # this order forms an edge between 2 chars
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # dict of visited?
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for nei_char in adj[char]:
                if dfs(nei_char):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for char in adj:
            # cycle
            if dfs(char):
                return ""
        
        return "".join(res[::-1])

        