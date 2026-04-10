class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        numSet = set(nums)
        res = []

        if not nums:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] - 1 not in numSet:
                    seen.add(nums[i]-1)

            for item in seen:
                length = 0
                val = item
                while val + 1 in numSet:
                    length += 1
                    val += 1
                res.append(length)
            return max(res)