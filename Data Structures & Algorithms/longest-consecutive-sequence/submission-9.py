class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        numSet = set(nums)

        if not nums:
            return 0
        else:
            for n in nums:
                if n-1 not in numSet:
                    seen.add(n-1)
            res = []
            for n in seen:
                length = 0
                val = n
                while val+1 in numSet:
                    length += 1
                    val = val + 1
                res.append(length)
            return max(res)
