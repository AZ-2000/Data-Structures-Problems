def generator(res, n, closed_cnt, open_cnt, stack):
    if open_cnt == closed_cnt == n:
        res.append("".join(stack))
        return
    else:
        if open_cnt < n:
            stack.append("(")
            generator(res, n, closed_cnt, open_cnt + 1, stack)
            stack.pop()
        if closed_cnt < open_cnt:
            stack.append(")")
            generator(res, n, closed_cnt+1, open_cnt, stack)
            stack.pop()

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        generator(res, n, 0, 0, [])
        return res


        

        