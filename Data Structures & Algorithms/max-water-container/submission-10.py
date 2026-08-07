class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxarea = 0

        while left < right:
            area = min(heights[left],heights[right]) * (right-left)
            maxarea = max(maxarea, area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        
        return maxarea