def is_palindrome(string):
    return string == string[::-1]

def backtrack(res,curr,idx, string):
    if idx == len(string):
        res.append(curr[:])
        return
    for i in range(idx, len(string)):
        cur = string[idx:i+1]
        if is_palindrome(cur):
            curr.append(cur)
            backtrack(res,curr, i+1, string)
            curr.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(res,[],0,s)
        return res