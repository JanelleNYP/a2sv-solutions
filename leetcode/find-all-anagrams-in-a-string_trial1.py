class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        p_count = Counter(p)
        window = Counter(s[:k])
        ans = []

        if k > n:
            return []

        if window == p_count:
            ans.append(0)
        
        for i in range(k , n):
            window[s[i]] += 1
            window[s[i-k]] -= 1

            if window[s[i-k]] == 0:
                del window[s[i-k]]
            if window == p_count:
                ans.append(i - k + 1)
        return ans