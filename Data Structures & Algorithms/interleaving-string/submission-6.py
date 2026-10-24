def bruteforce_dfs(s1, s2, s3,idx1, idx2, idx3, dp):
    if idx1 == len(s1) and idx2 == len(s2):
        return True
    if idx3 == len(s3):
        return False
    else:
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]
        if idx1 < len(s1) and s3[idx3] == s1[idx1]:
            if bruteforce_dfs(s1, s2, s3, idx1+1, idx2, idx3+1, dp):
                dp[idx1][idx2] = True
                return True
        if idx2 < len(s2) and s3[idx3] == s2[idx2]:
            if bruteforce_dfs(s1,s2,s3,idx1, idx2+1, idx3+1, dp):
                dp[idx1][idx2] = True
                return True
        dp[idx1][idx2] = False
        return False
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3 == "" and s1 == "" and s2 == "":
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        return bruteforce_dfs(s1,s2,s3, 0, 0,0, dp)
        
        