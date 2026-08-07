class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []
        for i in range(len(nums)):
            if not prefix:
                prefix.append(1)
            else:
                prefix.append(prefix[-1]*nums[i-1])
        
        for i in range(len(nums)-1,-1,-1):
            if not postfix:
                postfix.append(1)
            else:
                postfix.append(postfix[-1] * nums[i+1])
        j = len(nums)-1
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[j])
            j -= 1
        return res
        