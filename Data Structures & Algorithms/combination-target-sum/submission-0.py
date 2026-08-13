def helper(idx, ls, res, target,curr, summa):
    if idx == len(ls) or summa > target:
        return None
    if summa == target:
        res.append(curr[:])
        return
    curr.append(ls[idx])
    helper(idx, ls, res, target, curr, summa + ls[idx])
    curr.pop()
    helper(idx + 1,ls, res, target, curr, summa)
         
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        helper(0, nums,res, target, curr, 0)
        return res

        