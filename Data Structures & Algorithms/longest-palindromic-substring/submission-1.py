class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(len(s))]

        start = 0
        maxlen = 1

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                if maxlen == 1:
                    start = i
                    maxlen = 2
        
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > maxlen:
                        start = i
                        maxlen = length
        
        return s[start:start+maxlen]