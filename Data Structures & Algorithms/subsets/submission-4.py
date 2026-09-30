def helper(nums,idx,res,curr):
    if idx == len(nums):
        res.append(curr[:])
        return
    else:
        curr.append(nums[idx])
        helper(nums, idx+1, res,curr)
        curr.pop()
        helper(nums, idx+1, res, curr)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        helper(nums, 0, res, curr)
        return res
        
        