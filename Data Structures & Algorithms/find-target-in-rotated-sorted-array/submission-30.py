class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[r]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return mid
            elif nums[mid] > nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid
            elif nums[mid] < nums[l]:
                if nums[mid] < nums[r]:
                    if target <= nums[r] and target > nums[mid]:
                        l = mid
                    else:
                        r = mid - 1
            if mid == l:
                if nums[l] != target:
                    l += 1
        return -1

            


