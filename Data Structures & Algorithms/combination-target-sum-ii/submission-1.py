def helper(idx, ls, res, curr, target):
    if target == 0:
        res.append(curr[:])
        return 
    if target <0 or idx == len(ls):
        return
    
    for i in range(idx, len(ls)):
        if i > idx and ls[i] == ls[i-1]:
            continue
        
        curr.append(ls[i])
        helper(i+1, ls, res, curr, target - ls[i])
        curr.pop()


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        helper(0, candidates, res, [],  target)
        return res