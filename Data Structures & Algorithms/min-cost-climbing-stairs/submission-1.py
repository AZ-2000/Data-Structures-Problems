class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0,0
        for i in range(2, len(cost)+1):
            tmp = min(two+cost[i-2],one+cost[i-1])
            two = one
            one = tmp
        return tmp