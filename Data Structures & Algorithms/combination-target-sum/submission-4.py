def backtrack(idx, nums, target,res, curr, summa):
    if summa[0] > target:
        return
    elif summa[0] == target:
        res.append(curr[:])
        return
    elif idx == len(nums):
        return
    else:
        summa[0] += nums[idx]
        curr.append(nums[idx])
        backtrack(idx, nums, target, res, curr, summa)
        curr.pop()
        summa[0] -= nums[idx]
        backtrack(idx+1, nums, target, res, curr, summa)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        backtrack(0, nums, target, res, curr, [0])
        return res
        