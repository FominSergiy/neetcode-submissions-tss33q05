class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # add 1 from right to left
        # if less that 9, return right away
        # otherwise keep adding
        # if carry left, return carry
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            digit = digits[i]
            if digit < 9:
                digits[i] = digit + 1
                return digits
            digits[i] = (digit + carry) % 10
            carry = (digit + carry) // 10

        if carry:
            return [1] + digits
        return digits