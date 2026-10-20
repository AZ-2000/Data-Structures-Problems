def is_pallindrome(s):
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def backtrack(s, res, start, curr):
    if start == len(s):
        res.append(curr[:])
    else:
        for i in range(start, len(s)):
            substring = s[start:i+1]
            if is_pallindrome(substring):
                curr.append(substring)
                backtrack(s, res, i + 1, curr)
                curr.pop()
    return res

    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(s, res, 0, [] )
        return res