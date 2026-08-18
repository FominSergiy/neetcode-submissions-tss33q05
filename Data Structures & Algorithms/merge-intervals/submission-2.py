class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda item: item[0])
        output = [intervals[0]]
        # look forward to an overlapping interval, but sort first

        for start, end in intervals:
            last_end = output[-1][1]
            if last_end >= start: # overlap
                output[-1][1] = max(output[-1][1], end)
                output[-1][0] = min(output[-1][0], start)
            else:
                output.append([start, end])
        
        return output