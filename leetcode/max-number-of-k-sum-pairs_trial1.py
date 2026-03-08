class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        ans = 0

        for num in nums:
            if seen.get(k - num, 0) > 0:
                ans += 1
                seen[k - num] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return ans       