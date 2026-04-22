class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)

        res = 0
        
        left[0] = height[0]

        for i in range(len(height)):
            left[i] = max(left[i-1],height[i])
        right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1,-1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(1, len(height)-1):
            minima = min(left[i],right[i])
            res += minima - height[i]
        return res
