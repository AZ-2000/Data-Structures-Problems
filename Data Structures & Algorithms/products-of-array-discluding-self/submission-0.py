class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [] * len(nums)
        left = len(nums)//2 
        right = len(nums) //2 + 1
        prod = 1
        i = 0
        while i < len(nums):
            while left >=0 or right < len(nums):
                if left == i:
                    left -= 1
                    continue
                elif right == i:
                    right += 1
                    continue
                if right >= len(nums):
                    prod = prod * nums[left]
                    left -= 1
                    continue
                prod = prod*nums[left] * nums[right]
                left -= 1
                right += 1
            output.append(prod)
            prod = 1
            left = len(nums)//2 
            right = len(nums) //2 + 1
            i+=1
        
        return output
            
            

            
                

        





