class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        # brute force is to try any starting position and try to reach itself
        for start in range(n):
            gas_left = gas[start] - cost[start]
            next_stop = start + 1
            while gas_left > 0 and next_stop % n != start:
                # print(f"starting: {start}, gas: {gas_left}, at stop: {next_stop}")
                gas_left += gas[next_stop % n] - cost[next_stop % n]
                next_stop += 1
            
            # this means we got to the starting position
            if next_stop % n == start:
                # print(gas_left)
                return start
            else:
                continue
        
        