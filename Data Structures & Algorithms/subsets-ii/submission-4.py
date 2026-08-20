class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 2 ways 1, skip dups, 2nd count binary choices and pass forward

        # option 1, build as we go
        # def backtrack(i: int, cur: list[int]):
        #     ans.append(cur[:])

        #     if i == len(nums):
        #         return
            
        #     # build as we go and skip dups on THIS level
        #     for j in range(i, len(nums)):
        #         if j > i and nums[j] == nums[j - 1]:
        #             continue
                
        #         cur.append(nums[j])
        #         backtrack(j + 1, cur)
        #         cur.pop()


        # option 2 - build on choices
        def backtrack(i: int, cur: list[int]):
            if i == len(nums):
                ans.append(cur[:])
                return

            # choice of adding this number
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            # skip dups and select next one
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur)


        ans = []
        nums.sort()
        backtrack(0, [])
        return ans