class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.items(), key = lambda x: x[1], reverse=True)

        ans = ""
        for char, freq in sorted_chars:
            ans += char * freq

        return ans