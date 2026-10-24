def bruteforce_dfs(s1, s2, s3,idx1, idx2, idx3,res, curr, dp):
    if s3 == curr and idx1 == len(s1) and idx2 == len(s2):
        dp[idx1][idx2] = curr[:]
        return 
    if idx3 == len(s3):
        dp[idx1][idx2] = curr[:]
        return 
    else:
        if dp[idx1][idx2]:
            return dp[idx1][idx2]
        if idx1 < len(s1) and s3[idx3] == s1[idx1]:
            curr.append(s3[idx3])
            dp[idx1][idx2] = curr[:]
            bruteforce_dfs(s1, s2, s3, idx1+1, idx2, idx3+1, res, curr, dp)
            curr.pop()
        if idx2 < len(s2) and s3[idx3] == s2[idx2]:
            curr.append(s3[idx3])
            dp[idx1][idx2] = curr[:]
            bruteforce_dfs(s1,s2,s3,idx1, idx2+1, idx3+1, res, curr, dp)
            curr.pop()

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3 == "" and s1 == "" and s2 == "":
            return True
        res = []
        s3 = list(s3)
        dp = [["" for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        bruteforce_dfs(s1,s2,s3, 0, 0,0,res, [], dp)
        if dp[len(s1)][len(s2)]:
            return True
        else:
            return False
        
        