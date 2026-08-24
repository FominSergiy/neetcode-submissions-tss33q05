from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        

    def addNum(self, num: int) -> None:
        # add num to either based on fit to small or large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # rebalance from small to large if len + 1
        if len(self.small) > len(self.large) + 1:
            num = - 1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        # rebalance from large to small if len + 1
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * num)
        

    def findMedian(self) -> float:
        # if odd return largest list
        # even return avg of both
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0
        
        