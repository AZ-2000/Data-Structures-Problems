def dfs_backtracking(nums, target,idx, dp):
    if target == 0 and idx == len(nums):
        return 1
    if idx >= len(nums):
        return 0 
    else:
        key = (target, idx)
        if key in dp:
            return dp[key]
        dp[key] = 0
        dp[key] += dfs_backtracking(nums, target - nums[idx], idx + 1, dp)
        dp[key] += dfs_backtracking(nums, target + nums[idx], idx+1, dp)
    
    return dp[key]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return dfs_backtracking(nums, target, 0, dp)