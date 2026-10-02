def permutations(idx, nums, res):
    if idx == len(nums):
        res.append(nums[:])
        return
    else:
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            permutations(idx+1, nums, res)
            nums[idx], nums[i] = nums[i], nums[idx]
 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations(0, nums, res)
        return res
        
        