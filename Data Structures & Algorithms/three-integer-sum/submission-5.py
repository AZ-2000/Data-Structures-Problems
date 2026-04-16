class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,h in enumerate(nums):

            if i > 0 and h == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1

            while left < right:
                summa = nums[right] + nums[i] + nums[left]

                if summa > 0:
                    right -=1
                elif summa < 0:
                    left += 1
                else: #equals 0 or target
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return res