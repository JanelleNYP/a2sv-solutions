class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sub_avg = sum(nums[:k])/k
        max_avg = sub_avg

        for i in range(k, n):
            sub_avg += nums[i]/k
            sub_avg -= nums[i - k]/k

            max_avg = max(max_avg, sub_avg)

        return max_avg
            