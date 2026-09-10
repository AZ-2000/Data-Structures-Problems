class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            hashmap = {}
            l,r = 0,0
            count = 0
            for r in range(len(nums)):
                hashmap[nums[r]] = 1 + hashmap.get(nums[r],0) 

                while len(hashmap) > k:
                    hashmap[nums[l]] -= 1

                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]
                    l += 1
                count += r-l + 1
            return count
        return atMost(k) - atMost(k-1)









