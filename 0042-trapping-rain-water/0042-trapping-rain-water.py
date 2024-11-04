class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_high = right_high = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_high:
                    water += left_high - height[left]
                else:
                    left_high = height[left]
                left += 1
            else:
                if height[right] < right_high:
                    water += right_high - height[right]
                else:
                    right_high = height[right]
                right -= 1
        return water
