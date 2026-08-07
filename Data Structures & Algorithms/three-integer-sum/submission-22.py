class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            number = nums[i]
            left, right = i + 1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == -1 * number:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] + number < 0:
                    left += 1
                elif nums[left] + nums[right] + number > 0:
                    right -= 1
        return res
                
            

            