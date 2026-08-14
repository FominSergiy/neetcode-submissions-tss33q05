class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 2 ways 1, skip dups, 2nd count binary choices and pass forward

        def backtrack(i: int, cur: List[int]):
            ans.append(cur[:])

            if i == len(nums):
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                cur.append(nums[j])
                backtrack(j + 1, cur)
                cur.pop()
        

        ans = []
        nums.sort()
        backtrack(0, [])
        return ans