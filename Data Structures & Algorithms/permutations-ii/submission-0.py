def permute(idx, nums, res, seen):
    if idx == len(nums) and tuple(nums) not in seen:
        res.append(nums[:])
        seen.add(tuple(nums[:]))
        return
    else:
        for i in range(idx, len(nums)):
            nums[i],nums[idx] = nums[idx], nums[i]
            permute(idx+1, nums, res, seen)
            nums[idx],nums[i] = nums[i] , nums[idx]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        permute(0, nums,res, seen)
        return res