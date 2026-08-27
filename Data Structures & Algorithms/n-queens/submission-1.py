def backtrack(row,col,n,visited_c ,posdiag, negdiag, res, board):
    if row == n:
        copy = ["".join(r) for r in board]
        res.append(copy)
        return
    for c in range(n):
        if c in visited_c or (row+c in posdiag) or (row-c in negdiag):
            continue
        else:
            visited_c.add(c)
            posdiag.add(row+c)
            negdiag.add(row-c)
            board[row][c] = "Q" 
            backtrack(row+1, c, n,visited_c, posdiag, negdiag, res, board)
            visited_c.remove(c)
            posdiag.remove(row+c)
            negdiag.remove(row-c)
            board[row][c] = "."
 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posdiag = set()
        negdiag = set()
        visited_c = set()
        board = [['.'] *n for i in range(n)]
        backtrack(0,0, n,visited_c, posdiag, negdiag, res, board)
        return res