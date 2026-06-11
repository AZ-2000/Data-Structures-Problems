class Solution:
    def helper(self, nums, index,res):
        if index == len(nums)-1:
            res.append(list(nums))
            return 
        else:
            for i in range(index, len(nums)):
                nums[index],nums[i] = nums[i],nums[index]
                self.helper(nums,index + 1,res)
                nums[index],nums[i] = nums[i],nums[index]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res)
        return res

        