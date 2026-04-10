class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        print(hashmap)
        for key in hashmap:
            if hashmap[key] > len(nums) // 2:
                return key

        