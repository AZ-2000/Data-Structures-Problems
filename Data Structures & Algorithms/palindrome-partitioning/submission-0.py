def is_palindrome(s):
    return s == s[::-1]

def helper(idx,res, ls, curr):
    if idx == len(ls):
        res.append(curr[:])
        return 
    else:
        for i in range(idx, len(ls)):
            if is_palindrome(ls[idx:i+1]):
                curr.append(ls[idx:i+1])
                helper(i+1, res, ls, curr)
                curr.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        helper(0, res, s, [])
        return res