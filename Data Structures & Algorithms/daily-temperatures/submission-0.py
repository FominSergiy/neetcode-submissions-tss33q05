class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cur_temp_i = stack.pop()
                ans[cur_temp_i] = i - cur_temp_i
            stack.append(i)
        return ans