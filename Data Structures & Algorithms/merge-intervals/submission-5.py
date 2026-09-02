from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # SORT FIRST
        intervals.sort(key=lambda item: item[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            if output[-1][1] < start:
                output.append([start, end])
            else:
                output[-1][0] = min(output[-1][0], start)
                output[-1][1] = max(output[-1][1], end)
        return output
        # SWEEP LINE ALGO

        
        # return res
