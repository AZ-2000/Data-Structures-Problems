def backtrack(idx, nums, res, curr):
    if curr in res:
        return
    res.append(curr[:])
    for i in range(idx, len(nums)):
        curr.append(nums[i])
        backtrack(i+1, nums, res, curr)
        curr.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        backtrack(0, nums, res, curr)
        return res