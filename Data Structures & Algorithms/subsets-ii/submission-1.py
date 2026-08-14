def helper(idx, ls, res, curr, seen):
    if idx == len(ls):
        if tuple(sorted(curr)) not in seen:
            seen.add(tuple(sorted(curr[:])))
            res.append(curr[:])
            return res
        else:
            return 

    else:
        helper(idx + 1, ls, res, curr, seen)
        curr.append(ls[idx])
        helper(idx +1, ls, res, curr,seen)
        curr.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        helper(0, nums, res, [], seen)
        return res
        