class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 0
        maxprofit = 0

        while r < len(prices):
            summa = prices[r] - prices[l]
            if prices[r] - prices[l] <= 0:
                l = r
            
            maxprofit = max(maxprofit, summa)
            r += 1
        return maxprofit



