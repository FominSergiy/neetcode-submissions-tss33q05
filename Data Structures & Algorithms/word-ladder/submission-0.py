from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.can_transform(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        

        def dfs(node: str):
            nonlocal min_num
    
            queue = deque([(node, 0)])
            while queue:
                n, step = queue.popleft()
                step += 1

                if n == endWord:
                    min_num = min(min_num, step)
                    continue

                for nei in adj[n]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append([nei, step])
            return
        
        # start word dont have any nei
        if not adj[beginWord]:
            return 0

        visited = set()
        min_num = float("inf")

        visited.add(beginWord)
        dfs(beginWord)

        return 0 if min_num == float('inf') else min_num
        
    


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