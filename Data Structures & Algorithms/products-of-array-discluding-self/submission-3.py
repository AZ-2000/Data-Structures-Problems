class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        length = len(nums) + 1
        output = [0] * length
        output [0] = prefix
        for i in range(len(nums)):
            if i+1 == len(nums):
                break
            print(prefix, nums[i])
            output[i+1] = prefix * nums[i]
            prefix = output[i+1]
        
        for i in range(len(nums)-1,-1,-1):
            j = i + 1
            output[i] *= postfix 
            postfix *= nums[i]

        return output[0:len(nums)]
            
            

            
                

        





