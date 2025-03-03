class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = equal = 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1
        i, j, k = 0, less, less + equal
        result = [0] * len(nums)
        for num in nums:
            if num < pivot:
                result[i] = num
                i += 1
            elif num == pivot:
                result[j] = num
                j += 1
            else:
                result[k] = num
                k += 1
        return result
