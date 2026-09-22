class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = 0
        bestsum = float("-inf")

        for n in nums:
            currentsum = max(n, currentsum + n)
            bestsum = max(currentsum, bestsum)
        return bestsum
            