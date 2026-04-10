class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefix = []
        suffix = []
        output = []

        for i in range(len(nums)-1):
            if not prefix:
                prefix.append(1)
            prefix.append(prefix[-1]*nums[i])
        
        for i in range(len(nums)-1,0,-1):
            if not suffix:
                suffix.append(1)
            suffix.append(suffix[-1]*nums[i])
        
        for i in range(len(nums)):
            output.append(suffix[-1] * prefix[i])
            suffix.pop()
        print(output)
        return output