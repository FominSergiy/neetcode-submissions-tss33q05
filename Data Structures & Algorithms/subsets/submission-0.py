class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        cur = []

        def backtrack(i: int):
            ans.append(cur[:])
            if i == len(nums):
                return

            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()
        
        backtrack(0)
        return ans