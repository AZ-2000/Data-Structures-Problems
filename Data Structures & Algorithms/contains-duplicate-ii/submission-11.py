class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l, r =0,1
        window.add(nums[0])
        while r < len(nums):
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
                if r - l >=k:
                    window.remove(nums[l])
                    l += 1
            r += 1
        return False



        