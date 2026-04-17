class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        for i,v in hashmap.items():
            freq[v].append(i)      

        res = []
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        

