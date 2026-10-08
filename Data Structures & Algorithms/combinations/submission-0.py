def backtrack(n, nums, k, idx, res, curr):
    if len(curr) == k:
        res.append(curr[:])
        return
    else:
        for i in range(idx, n):
            curr.append(nums[i])
            backtrack(n, nums, k, i+1, res, curr)
            curr.pop()

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        res = []
        curr = []
        backtrack(n, nums, k, 0, res, curr)
        return res