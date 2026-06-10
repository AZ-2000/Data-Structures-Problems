class Solution:
    def helper(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.helper(nums, mid+1, right, target)
        elif nums[mid] > target:
            return self.helper(nums,left, mid-1, target)
        
        
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)
       