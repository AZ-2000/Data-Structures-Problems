class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin = 1
        currmax = 1
        bestsol = max(nums)
        for n in nums:
            if n == 0:
                currmin, currmax = 1,1
                continue
            tmp = currmax * n
            currmax = max(n, currmax*n, currmin *n)
            currmin = min(n, currmin*n, tmp)
            bestsol = max(bestsol, currmax)
        return bestsol


        