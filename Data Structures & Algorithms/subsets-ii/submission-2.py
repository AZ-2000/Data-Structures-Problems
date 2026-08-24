def subsetsII(nums, idx, res, curr):
    res.append(curr[:])
    if idx == len(nums):
        return
    
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        curr.append(nums[i])
        subsetsII(nums, i+1, res, curr)
        curr.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsetsII(nums, 0, res, [])
        return res
        