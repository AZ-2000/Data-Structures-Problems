class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0

        mid = len(nums)//2
        print(mid)
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (right+left)//2
            elif nums[mid] > target:
                right = mid - 1
                mid = (right+left) // 2
        
        return -1





