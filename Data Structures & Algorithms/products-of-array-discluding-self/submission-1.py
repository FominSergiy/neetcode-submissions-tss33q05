class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n^2)
        # n = len(nums)
        # output = [0] * n
        # for i in range(n):
        #     prd = 1
        #     for j in range(n):
        #         if i != j:
        #             prd *= nums[j]
        #     output[i] = prd
        # return output

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        output = [1] * n
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output

