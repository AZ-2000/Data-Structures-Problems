class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summa = nums[left] + nums[right] + nums[i]
                if summa > 0:
                    right -= 1
                elif summa < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return res
                    

            