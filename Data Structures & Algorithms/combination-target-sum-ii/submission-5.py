def combsum(nums, idx, target, curr, res):
    if target == 0:
        res.append(curr[:])
    if target <0 or idx == len(nums):
        return
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        curr.append(nums[i])
        combsum(nums, i+1, target - nums[i], curr, res )
        curr.pop()


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combsum(candidates, 0, target, [], res)
        return res


