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
        if self.large and len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * num)

        # rebalance from large to small if len + 1
        if self.small and len(self.small) > len(self.large) + 1:
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)

        
    def findMedian(self) -> float:
        n_large, n_small = len(self.large), len(self.small)

        if n_large > n_small:
            return self.large[0]
        elif n_small > n_large:
            return -1 * self.small[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2

        
        