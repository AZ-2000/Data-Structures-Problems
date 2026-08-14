def helper(res, open_cnt, closing_cnt, n,stack):
    if open_cnt == closing_cnt ==n:
        res.append("".join(stack))
        return
    else:
        if open_cnt<n:
            stack.append("(")
            helper(res, open_cnt + 1, closing_cnt, n, stack)
            stack.pop()
        if closing_cnt<open_cnt:
            stack.append(")")
            helper(res, open_cnt, closing_cnt+1, n, stack)
            stack.pop()




        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        helper(res, 0,0,n, [])
        return res
        

        