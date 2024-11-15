class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        lend, rend = 1, len(arr)
        arr.append(-1)
        while arr[lend - 1] <= arr[lend]:
            lend += 1
        if lend == rend:
            return 0
        left, right = 0, rend - 1
        while arr[right - 1] <= arr[right]:
            right -= 1
        result = min(rend - lend, right)
        while left < lend and right < rend:
            if arr[left] <= arr[right]:
                left += 1
                result = min(result, right - left)
            else:
                right += 1
        return result
