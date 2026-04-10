class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        suff = [0] * len(nums)
        res = []

        for i in range(len(nums)):
            if i == 0:
                pre.append(1)
                j = 0
            else:
                pre.append(nums[i-1] * pre[j])
                j += 1

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                suff[i] = 1
                j = len(nums) - 1
            else:
                suff[i] = nums[i+1] * suff[j]
                j -= 1

        for i in range(len(nums)):
            res.append(pre[i] * suff[i])
                
        return res
        





