def helper(idx, ls,res, curr):
    #base case
    if idx == len(ls):
        res.append(curr[:]) #not simply curr, we used curr[:] since otherwise
                            #the list inside res would mutate too!
    else:
        #recursive step
        helper(idx + 1, ls,res,curr)
        curr.append(ls[idx])
        helper(idx + 1, ls, res, curr)
        curr.pop()
    return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        res = helper(0, nums, res, curr)
        return res