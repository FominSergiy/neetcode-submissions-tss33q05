class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        n = len(nums)

        def backtrack(i: int, cur_sum):
            # print(f"i:{i}, cur_sum: {cur_sum}")
            if sum(cur_sum) == target:
                ans.append(cur_sum[:])


            if sum(cur_sum) > target:
                return

            for j in range(i, n):
                # add a number
                cur_sum.append(nums[j])
                backtrack(j, cur_sum)
                cur_sum.pop()
        
        backtrack(0, [])
        return ans