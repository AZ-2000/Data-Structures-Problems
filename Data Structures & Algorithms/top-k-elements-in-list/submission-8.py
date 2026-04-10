class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hashmap [i] = 1 + hashmap.get(i, 0)

        for key, value in hashmap.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)

                if len(res) == k:
                    return res