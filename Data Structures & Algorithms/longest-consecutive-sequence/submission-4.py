class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = []
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                seen.add(nums[i]-1)

        for item in seen:
            length = 0
            val = item
            while val + 1 in nums:
                length += 1
                val += 1
            res.append(length)
        print(res)
        return max(res)
                
            



        




        
             
