class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(1, n):
            colour = nums[i]

            j = i - 1

            while j >= 0 and nums[j] > colour:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = colour
        
        return nums
        