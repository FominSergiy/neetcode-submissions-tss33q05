class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # find all intervals before
        # find overlapping and get i: j of it and build the bounds
        # find all after

        # res = []
        # # get before merge
        # i = 0
        # while i < len(intervals) and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1

        # # get the merge elements
        # while i < len(intervals) and newInterval[1] >= intervals[i][0]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)
        # res = res + intervals[i:]
        # return res

        # greedy solutions are all about making local, small choices that affect the outcome
        # in this case it is about 3 choices we can make as we iterate over the intervals
        res = []

        for i in range(len(intervals)):
            # if new interval ends before the current starts
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new interval is way ahead of current one
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # merge otherwise
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res

        