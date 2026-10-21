def backtrack(nums, target, idx, dp):
    if idx == len(nums):
        if target == 0:
            return 1
        else:
            return 0
    else:
        key = (idx, target)
        if key in dp:
            return dp[key]
        else:
            dp[key] = 0
            dp[key] += backtrack(nums, target - nums[idx], idx + 1, dp)
            dp[key] += backtrack(nums, target + nums[idx], idx + 1, dp)
    
    return dp[key]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        curr = []
        arr = []
        return backtrack(nums, target, 0, dp)
        