class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = []
        n = len(position)

        for i in range(n):
            # how many moves needed to reach end
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse=True)

        stack = []
        for pos, speed in pairs:
            
            stack.append((target - pos) / speed)
            print(f"before:{stack}")
            # append new car to the fleet
            # if this car's arrival time is faster than the last next item in the stack
            # we can pop it - meaning it has arrived and 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            print(f"after: {stack}")
        
        return len(stack)