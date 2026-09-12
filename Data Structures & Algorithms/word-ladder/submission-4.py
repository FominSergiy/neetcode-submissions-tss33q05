from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        n = len(wordList)
        
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                w1, w2 = wordList[i], wordList[j]
                if self.can_transform(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)
        
        queue = deque([(0, beginWord)]) # (steps, word)
        ans = float('inf')
        visited = set()
        while queue:
            steps, node = queue.popleft()

            if node == endWord:
                ans = min(ans, steps + 1)
            
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((steps + 1, nei))
    
        return ans if ans != float('inf') else 0


    def can_transform(self, word_a: str, word_b: str) -> bool:
        i = 0
        diff = 0
        while i < len(word_a):
            if word_a[i] != word_b[i]:
                diff += 1
            
            if diff > 1:
                return False
            i += 1
        return True
