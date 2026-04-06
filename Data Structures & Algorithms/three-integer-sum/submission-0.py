class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        n = len(nums)
        for i in range(n - 2):
            # dups for outer loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = n - 1
            target = -nums[i]
            
            while low < high:
                if nums[low] + nums[high] == target:
                    triplets.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    # skip low dups
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1
                    
                    # skip high dups
                    while nums[high] == nums[high + 1] and low < high:
                        high -= 1

                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1
        
        return triplets
