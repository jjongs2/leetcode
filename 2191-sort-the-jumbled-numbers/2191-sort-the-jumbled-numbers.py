class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            if num == 0:
                return mapping[0]
            result = 0
            multiplier = 1
            while num > 0:
                result += mapping[num % 10] * multiplier
                multiplier *= 10
                num //= 10
            return result

        mapped_nums = ((convert(num), i) for i, num in enumerate(nums))
        return [nums[i] for _, i in sorted(mapped_nums)]
