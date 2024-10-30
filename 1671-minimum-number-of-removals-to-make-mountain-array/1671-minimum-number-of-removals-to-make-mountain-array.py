from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        mt_lengths = [-1 for _ in range(n)]
        lis = [nums[0]]
        for i in range(1, n - 1):
            num = nums[i]
            if num > lis[-1]:
                lis.append(num)
            else:
                lis[bisect_left(lis, num)] = num
            if len(lis) > 1:
                mt_lengths[i] += len(lis)
        lds = [nums[-1]]
        for i in range(n - 2, 0, -1):
            num = nums[i]
            if num > lds[-1]:
                lds.append(num)
            else:
                lds[bisect_left(lds, num)] = num
            if mt_lengths[i] > -1 and len(lds) > 1:
                mt_lengths[i] += len(lds)
        return n - max(mt_lengths)
