class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = []
        if not nums:
            return 0
        for i in range(len(nums)):
            k = nums[i]-1
            if k in nums:
                continue
            else:
                seen.add(k)

        for num in seen:
            length = 0
            while num + 1 in nums:
                length += 1
                num += 1
            res.append(length)
        return max(res)
            



        




        
             
