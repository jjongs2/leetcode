class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while (width := right - left) > 0:
            if height[left] < height[right]:
                area = max(area, width * height[left])
                left += 1
            else:
                area = max(area, width * height[right])
                right -= 1
        return area
