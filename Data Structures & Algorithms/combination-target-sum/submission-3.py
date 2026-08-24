def combsum(idx, nums, target, summa,res, curr):
    if idx == len(nums) or summa > target:
        return
    elif summa == target:
        res.append(curr[:])
        return
    
    curr.append(nums[idx])
    combsum(idx, nums, target, summa + nums[idx], res, curr)
    curr.pop()
    combsum(idx+1, nums, target, summa, res, curr)


    


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combsum(0, nums, target, 0, res, [])
        return res
        