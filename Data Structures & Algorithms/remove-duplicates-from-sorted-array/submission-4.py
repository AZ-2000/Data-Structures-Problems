class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        count = 0
        while l < r:
            while l < len(nums)-1 and nums[l] == nums[l+1]:
                nums[l] = -101
                l += 1
            while r >= 0 and nums[r] == nums[r-1]:
                nums[r] = -101
                r -= 1
            l += 1
            r -=1
        i = 0
        print(nums)
        length = len(nums) - 1
        while i < length:
            if nums[i] == -101:
                del nums[i]
                i -= 1
                length -= 1
            i += 1
        if nums[len(nums)-1] == -101:
            del nums[len(nums)-1]
        return len(nums)
