def helper(nums,idx, target, summa, curr, res):
    if idx == len(nums):
        return
    if summa >= target:
        if summa == target:
            res.append(curr[:])
            return
        else:
            return 
    curr.append(nums[idx])
    helper(nums, idx, target, summa + nums[idx] , curr, res)
    curr.pop()
    helper(nums, idx+1, target, summa, curr, res)



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        summa = 0
        curr = []
        res = []

        helper(nums,0, target, summa, curr,res)
        return res
        