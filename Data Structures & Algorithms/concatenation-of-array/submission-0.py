class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * 2*len(nums)
        ans[0:len(nums)] = nums[0:len(nums)]
        ans[len(nums): 2*len(nums) - 1] = nums[0:len(nums)]
        return ans
        
            