class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+1)]
        res = []
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for key, value in hashmap.items():
            freq[value].append(key)

        for i in range(len(freq)-1,-1,-1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
        
        
        
        



