class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, h in enumerate(nums):
            if i>0 and h == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:

                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[right] + nums[left] + nums[i] > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1            
        return res
