class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)) % 2 == 1:
            return False 
        else:
            target = sum(nums)/2
            dp = set()
            dp.add(0)
            if target in nums:
                return True
            else:
                for i in range(len(nums)-1, -1,-1):
                    next_dp = set()
                    for t in dp:
                        if (t+nums[i]) == target:
                            return True
                        else:
                            next_dp.add(t+nums[i])
                            next_dp.add(t)
                    dp = next_dp
                return False




