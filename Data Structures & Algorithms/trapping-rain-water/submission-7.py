class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        rightmax = height[right]
        leftmax = height[left]
        res = 0

        while left<right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(height[left],leftmax)
                res += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(height[right], rightmax)
                res += rightmax - height[right]
        return res