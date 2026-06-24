class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r =0, 1

        while r < len(prices):
            profit = prices[r]-prices[l]
            if prices[l] >= prices[r]:
                l = r
            r+= 1
            maxProfit = max(maxProfit, profit)
        return maxProfit