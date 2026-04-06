class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        smaller_ptr = 0
        bigger_ptr = len(numbers) - 1

        while smaller_ptr <= bigger_ptr:
            cur_sum = numbers[smaller_ptr] + numbers[bigger_ptr]

            if cur_sum == target:
                return [smaller_ptr + 1, bigger_ptr + 1]
            elif cur_sum > target:
                bigger_ptr -= 1
            else:
                smaller_ptr += 1