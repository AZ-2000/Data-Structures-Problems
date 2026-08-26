def generator(n,open_cnt, closed_cnt, res, stack):
    if open_cnt == closed_cnt == n:
        res.append("".join(stack))
        return
    
    if open_cnt < n:
        stack.append("(")
        generator(n, open_cnt+1, closed_cnt, res, stack)
        stack.pop()
    if closed_cnt < open_cnt and closed_cnt < n:
        stack.append(")")
        generator(n, open_cnt, closed_cnt+1, res, stack)
        stack.pop()

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        generator(n, 0, 0, res, [])
        return res

        
        

        