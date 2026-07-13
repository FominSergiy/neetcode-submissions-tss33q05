# class TreeNode:
#     def __init__(self, val=None, is_end=False):
#         self.children
#         self.is_end = is_end
## { None: {next-obj}, is_end: False }

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # set to true once we have exhausted all chars
        cur.end_of_word = True
            


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        