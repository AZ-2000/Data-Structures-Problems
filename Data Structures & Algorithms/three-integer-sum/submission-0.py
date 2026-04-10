class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                print(left, right)
                sumnums = nums[i] + nums[left] + nums[right]
                listnums = [nums[i], nums[left],nums[right]]
                if listnums in res:
                    left += 1
                    right -= 1
                    continue
                if sumnums == 0: 
                    res.append(listnums)
                    left += 1 
                    right -= 1
                elif sumnums > 0:
                    right -= 1
                elif sumnums < 0:
                    left += 1
        return res
