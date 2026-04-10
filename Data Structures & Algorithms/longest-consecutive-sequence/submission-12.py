class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        numSet = set(nums)
        if not nums:
            return 0
        for n in nums:
            if n-1 not in seen:
                seen.add(n-1)
        res = []
        for dec in seen:
            length = 0
            val = dec
            while val+1 in numSet:
                length += 1
                res.append(length)
                val += 1
        return max(res)