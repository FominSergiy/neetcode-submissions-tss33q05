class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # find all intervals before
        # find overlapping and get i: j of it and build the bounds
        # find all after

        # iterative
        # 1. find all before
        # 2. merge the overlaps
        # 3. add all after
        ans = []

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # now the merger
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        ans.append(newInterval)
        return ans + intervals[i:]

   


        # # greedy
        # ans = []
        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         ans.append(newInterval)
        #         return ans + intervals[i:]
        #     if newInterval[0] > intervals[i][1]:
        #         ans.append(intervals[i])
        #     else:
        #         newInterval[0] = min(intervals[i][0], newInterval[0])
        #         newInterval[1] = max(intervals[i][1], newInterval[1])
        
        # ans.append(newInterval)
        # return ans
        # # 1. too early, add to list and return EARLY
        #     # return only in this branch
        # # 2. too late, just add current one
        # # 3. it is a merge - merge the interval

        # # add interval and return

        