def backtrack(prices, idx, buy, dp):    
    if idx >= len(prices):
        return 0
    else:
        if dp[idx][buy] != -1:
            return dp[idx][buy]
         #if we have the OPTION to buy
        if buy:   
            take = -prices[idx] + backtrack(prices, idx+1, 0, dp)
            skip = backtrack(prices,idx+1, 1, dp)
            dp[idx][buy] = max(take, skip)
         #if we have the OPTION to sell
        else:
            sell = prices[idx] + backtrack(prices, idx+2,1, dp)
            skip = backtrack(prices,idx+1, 0, dp)
            dp[idx][buy] = max(sell ,skip)
        return dp[idx][buy]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return backtrack(prices, 0, 1, dp)
        
        




