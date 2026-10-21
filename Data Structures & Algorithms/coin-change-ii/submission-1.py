def backtrack(amount, coins, idx, dp):
    if amount == 0:
        return 1
    if idx >= len(coins) or amount < 0:
        return 0
    else:
        if dp[amount][idx] != -1:
            return dp[amount][idx] 
        dp[amount][idx] = 0
        dp[amount][idx] += backtrack(amount - coins[idx], coins, idx,dp)
        dp[amount][idx] += backtrack(amount, coins, idx+1, dp)
    return dp[amount][idx]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(len(coins))] for _ in range(amount+1)]
        return backtrack(amount, coins, 0, dp)
