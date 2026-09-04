from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)

        # build adj graph
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.can_transform(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        # starting word has no adj nodes
        if not adj[beginWord]:
            return 0
        
        # else, lets find
        min_steps = float('inf')
        queue = deque([(beginWord, 0)])
        visited = set()

        while queue:
            node, step = queue.popleft()
            
            if node == endWord:
                min_steps = min(min_steps, step + 1) # count this node
            
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, step + 1))
        
        return min_steps if min_steps != float('inf') else 0

    


    def can_transform(self, word_a: str, word_b: str) -> bool:
        i = 0
        different = 0
        while i < len(word_a):
            if word_a[i] != word_b[i]:
                different += 1
            
            if different > 1:
                return False
            
            i += 1
        return True