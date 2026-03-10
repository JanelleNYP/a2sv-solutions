class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        seen = set()
        left = 0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[i])
            window_size = i - left + 1
            longest = max(longest, window_size)

        return longest

