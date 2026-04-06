from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for key,val in s_count.items():
            if key not in t_count or t_count[key] != val:
                return False
        return True
         