class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        for i in range(k):
            max_key_val_pair = max(hashmap.items(), key = lambda item: item[1])
            res.append(max_key_val_pair[0])
            del hashmap[max_key_val_pair[0]]
        
        return res



