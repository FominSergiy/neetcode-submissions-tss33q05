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
                if self.can_transform(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        
        queue = deque([(beginWord, 0)])
        min_steps = float('inf')
        visited = set()
        while queue:
            node, steps = queue.popleft()

            if node == endWord:
                min_steps = min(min_steps, steps + 1)
            
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))
        
        return min_steps if min_steps != float('inf') else 0


    


    def can_transform(self, word_a: str, word_b: str) -> bool:
        diff = 0
        i = 0
        while i < len(word_a):
            if word_a[i] != word_b[i]:
                diff += 1
            
            if diff > 1:
                return False

            i += 1
        return True