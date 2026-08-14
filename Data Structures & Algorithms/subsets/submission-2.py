def helper(idx,ls, res, curr):
    if idx == len(ls):
        res.append(curr[:])
        return res
    else:
        helper(idx + 1,ls,res, curr)
        curr.append(ls[idx])
        helper(idx + 1, ls, res, curr)
        curr.pop()


    


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        helper(0, nums, res, [])
        return res
        