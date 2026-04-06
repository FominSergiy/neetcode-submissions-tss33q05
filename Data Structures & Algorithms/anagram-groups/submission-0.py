from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hash_map = defaultdict(list)

        for word in strs:
            w_sorted = "".join(sorted(word))
            hash_map[w_sorted].append(word)
        
        ans = []

        for grouping in hash_map.values():
            ans.append(grouping)
        
        return ans