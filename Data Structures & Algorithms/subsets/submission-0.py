def helper(left, ls, res, curr):
    if left == len(ls):
        res.append(curr[:])
        return
    else:
        helper(left+1,ls, res,curr)
        curr.append(ls[left])
        helper(left+1,ls, res ,curr)
        curr.pop()



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        helper(0, nums, res, curr)
        return res