class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        n = len(nums)

        def backtrack(i: int, cur: list[int], total: int):
            if total == target:
                ans.append(cur[:])

            for j in range(i, n):
                # add a number
                if total + nums[j] > target:
                    continue
                cur.append(nums[j])
                backtrack(j, cur, total + nums[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return ans