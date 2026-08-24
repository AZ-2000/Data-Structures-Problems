def helper(idx, nums, res, curr):
    if idx == len(nums):
        res.append(curr[:])
        return

    helper(idx +1, nums,res,curr)
    curr.append(nums[idx])
    helper(idx+1, nums, res, curr)
    curr.pop()


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        helper(0, nums,res,[])
        return res
        
        