class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * (len(nums)-1)
        dp[0] = nums[1]
        dp[1] = max(dp[0], nums[2])
        
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-2]+nums[i+1],dp[i-1])
        tmp = dp[-1]
        
        dp = [0] * (len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        tmp = max(tmp, dp[-1])
        return tmp


            



        