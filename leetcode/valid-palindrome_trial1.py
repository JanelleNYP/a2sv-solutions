class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanum = ""

        for ch in s:
            if ch.isalnum():
                s_alphanum += ch.lower()

        return s_alphanum == s_alphanum[::-1]