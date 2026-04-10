class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for x in nums:
            print(seen)
            if x in seen:
                return True
            seen.add(x)
        return False 