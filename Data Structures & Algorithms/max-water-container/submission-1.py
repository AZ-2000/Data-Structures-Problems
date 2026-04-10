class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        if len(heights) == 2 and 0 in heights:
            return 0
        while left < right:
            min_val = min(heights[left], heights[right])
            area = min_val * (right - left)
            if area >= maxArea:
                maxArea = area
            if min_val == heights[right]:
                right -= 1
            elif min_val == heights[left]:
                left += 1
        return maxArea