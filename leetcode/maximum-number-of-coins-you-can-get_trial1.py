class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        n = len(piles)
        piles = sorted(piles)
        num_reps = n//3
        count = 0

        for i in range(n-2, -1, -2):
            ans += piles[i]
            count += 1
            if count == num_reps:
                break

        return ans    