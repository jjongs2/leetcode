class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_count = len(nums)
        answer = [1 for _ in range(num_count)]
        prefix_product = 1
        for i in range(num_count):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in range(num_count - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        return answer
