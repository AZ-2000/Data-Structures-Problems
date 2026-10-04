def generator(o, c, n, res, curr):
    if o == c == n:
        res.append("".join(curr))
        return
    if o >= c and o < n:
        curr.append("(")
        generator(o+1, c, n, res, curr)
        curr.pop()
        curr.append(")")
        generator(o, c+1, n, res, curr)
        curr.pop()
    if o == n and c < n:
        curr.append(")")
        generator(o, c+1, n, res, curr)
        curr.pop()
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        generator(0,0, n, res, curr)
        return res

        
        

        