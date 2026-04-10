class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefix = []
        suffix = []
        output = []

        for i in range(len(nums)):
            if not prefix:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] * nums[i-1])
        for i in range(len(nums),0,-1):
            if not suffix:
                suffix.append(1)
            else:
                print(nums[i])
                suffix.append(suffix[-1]*nums[i])
        
        for i in range(len(prefix)):
            output.append(suffix[-1] * prefix[i])
            suffix.pop()
        return output




