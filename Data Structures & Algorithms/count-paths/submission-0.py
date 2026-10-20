def traverse(dp,m,n):
    for i in range(1,len(dp)):
        for j in range(1,len(dp[i])):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m][n]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for i in range(m+1)]
        dp[0][0] = 0
        dp[0][1] = 1
        dp[1][0] = 1
        return int(traverse(dp,m,n)/2)
