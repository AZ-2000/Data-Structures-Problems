class Solution:
    def trap(self, height: List[int]) -> int:



        left = 0
        maxleft = height[left]
        right = len(height) - 1
        maxright = height[right]
        res = 0

        while left < right:

            if maxleft < maxright:
                left += 1
                maxleft = max(height[left], maxleft)
                res += maxleft - height[left]
                
            else:
                right -= 1
                maxright = max(height[right], maxright)
                res += maxright-height[right]
                

        return res




                       

