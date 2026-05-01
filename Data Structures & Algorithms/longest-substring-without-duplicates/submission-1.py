class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
            
        char_set = set()

        left = 0
        char_set.add(s[0])

        ans = 1

        for right in range(1, len(s)):
            while s[right] in char_set:
                # shrink left
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            ans = max(ans, len(char_set))

        return ans
            


        