class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanumeric = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(only_alphanumeric) - 1

        while left <= right:
            if only_alphanumeric[left] != only_alphanumeric[right]:
                return False
            left += 1
            right -= 1
        return True