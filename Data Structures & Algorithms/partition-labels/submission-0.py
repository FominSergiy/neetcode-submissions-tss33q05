from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # build a map of chars and their last indicies
        # as we move from left to right, constantly update the end value
        # once end is same as current i, this is the end of current sub-str, start new
        last_idx_map = defaultdict(int)
        for i in range(len(s)):
            last_idx_map[s[i]] = max(i, last_idx_map[s[i]])
        
        end = 0
        cur_size = 0
        output = []
        for i in range(len(s)):
            char = s[i]
            end = max(end, last_idx_map[char])
            cur_size += 1
            
            if end == i:
                output.append(cur_size)
                cur_size = 0
                continue
        
        return output