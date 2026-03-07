class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001

        for num in arr1:
            count[num] += 1
        
        result = []

        for num in arr2:
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        for i in range(len(count)):
            while count[i] > 0:
                result.append(i)
                count[i] -= 1

        return result