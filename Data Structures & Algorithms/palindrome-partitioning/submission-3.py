def is_palindrome(string):
    return string[::-1] == string

def partitioner(string, idx, res, curr):
    if idx == len(string):
        res.append(curr[:])
        return
    else:
        for i in range(idx, len(string)):
            cur = string[idx: i + 1]
            if is_palindrome(cur):
                curr.append(cur)
                partitioner(string, i+1, res, curr)
                curr.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitioner(s, 0, res, [])
        return res