def backtrack(idx, candidates, target, res, curr):
    if target == 0:
        res.append(curr[:])
        return
    if idx == len(candidates) or target < 0:
        return
    else:
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            curr.append(candidates[i])
            backtrack(i+1, candidates, target - candidates[i], res, curr)
            curr.pop()
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        backtrack(0, candidates, target, res, curr)
        return res
        