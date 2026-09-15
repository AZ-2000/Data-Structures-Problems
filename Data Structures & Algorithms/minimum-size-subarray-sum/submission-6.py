class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = set()
        l,r = 0, 1
        window = nums[0]
        minlength = float("infinity")
        for i in range(len(nums)):
            if nums[i] >= target:
                return 1

        while r < len(nums):
            window += nums[r]
            if window >= target:
                minlength = min(minlength, r-l+1)
            while window >= target:
                window -= nums[l]
                # print(sum(window), window)
                minlength = min(minlength, r-l+1)
                l += 1
            r += 1
        
        if minlength == float("infinity"):
            return 0
        else:
            return minlength



