class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)

        res = []
        for key, value in freq.items():
            if value > len(nums)//3:
                res.append(key)
        return res