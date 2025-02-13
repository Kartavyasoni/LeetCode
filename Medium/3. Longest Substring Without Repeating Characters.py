class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        left = 0
        right = 0
        chars_set = set()

        while right < len(s):
            if s[right] not in chars_set:
                chars_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                chars_set.remove(s[left])
                left += 1

        return max_length
