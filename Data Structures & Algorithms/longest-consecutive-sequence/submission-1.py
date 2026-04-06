class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest = float('-inf')

        if not nums:
            return 0

        for num in nums:
            if num - 1 not in set_nums:
                # start of the subsequence
                cur_longest = 1
                next_num = num + 1

                while next_num in set_nums:
                    cur_longest += 1
                    next_num += 1

                longest = max(longest, cur_longest)
        
        return longest