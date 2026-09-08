class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob_1, rob_2 = 0,0
        rob_i, rob_ii =0,0

        for i in range(1, len(nums)):
            tmp = max(nums[i] + rob_1, rob_2)
            rob_1 = rob_2
            rob_2 = tmp
        for i in range(len(nums)-1):
            tmp = max(nums[i] + rob_i, rob_ii)
            rob_i = rob_ii
            rob_ii = tmp
        return max(rob_ii, rob_2)



        