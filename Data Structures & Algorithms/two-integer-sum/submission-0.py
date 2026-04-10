class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                print(hashmap)
                res.append(hashmap[complement])
                res.append(i)
                return res
            hashmap[nums[i]] = i


        