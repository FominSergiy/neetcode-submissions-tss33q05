from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += ceil(pile / speed)
            
            return hours <= h

        
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        
            
        