class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0
        for i in range(2,len(cost)+1):
            tmp = min(one + cost[i-2], two + cost[i-1])
            one = two
            two = tmp
        return tmp