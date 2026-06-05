class Solution:
    def helper(self,nums, left, right, target):
        if left > right:
            return - 1
        middle = (left + right)//2
        if nums[middle] == target:
            return middle
        else:
            if target <nums[middle]:
                return self.helper(nums, left, middle-1, target)
            else:
                return self.helper(nums, middle + 1, right, target)
            
    def search(self, nums: List[int], target: int) -> int:
       return self.helper(nums,0, len(nums)-1,target)