def permutation(nums, idx, res):
    if idx == len(nums)-1:
        res.append(list(nums))
        return
    else:
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            permutation(nums, idx + 1, res)
            nums[idx], nums[i] = nums[i], nums[idx]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        permutation(nums, 0, res)
        return res
        
        