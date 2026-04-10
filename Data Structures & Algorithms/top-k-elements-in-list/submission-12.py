class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(list)
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        for key, value in hashmap.items():
            freq[value].append(key)
        
        res = []
        print(freq)
        for i in range(len(nums),-1,-1):
            for j in freq[i]:
                print(j)
                res.append(j)
                if len(res) == k:
                    return res