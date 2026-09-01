from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # build a map of chars and their last indicies
        # as we move from left to right, constantly update the end value
        # once end is same as current i, this is the end of current sub-str, start new
        val_to_last_idx = defaultdict(int)
        
        for i in range(len(s)):
            char = s[i]
            val_to_last_idx[char] = max(i, val_to_last_idx[char])
        
        size = 0
        end = 0
        output = []
        for i in range(len(s)):
            size += 1
            char = s[i]
            end = max(end, val_to_last_idx[char])

            if end == i:
                output.append(size)
                end = 0
                size = 0
        
        return output
