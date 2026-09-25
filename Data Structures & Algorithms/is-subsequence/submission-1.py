class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = []
        if not s:
            return True
        for c in s:
            memo.append(c)
        idx = 0
        for c in t:
            if memo[idx] == c:
                memo[idx] = True
                idx += 1
            if idx == len(memo):
                return True
        for item in memo:
            if item != True:
                return False
        return True            