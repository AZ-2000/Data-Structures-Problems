def is_pallindrome(s):
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
def backtrack(s, res, curr, start):
    if start == len(s):
        res.append(curr[:])
        return
    else:
        for i in range(start, len(s)):
            substr = s[start:i+1]
            if is_pallindrome(substr):
                curr.append(substr)
                backtrack(s,res,curr, i+1)
                curr.pop()

    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(s, res, [], 0)
        return res