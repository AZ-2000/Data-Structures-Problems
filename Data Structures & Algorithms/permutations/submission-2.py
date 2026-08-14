def helper(idx, ls, res):
    if idx == len(ls)-1:
        res.append(list(ls))
        return 
    else:
        for i in range(idx, len(ls)):
            ls[idx], ls[i] = ls[i], ls[idx]
            helper(idx+1,ls, res)
            ls[idx], ls[i] = ls[i], ls[idx]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        helper(0, nums, res)
        return res
