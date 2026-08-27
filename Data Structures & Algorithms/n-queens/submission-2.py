def backtrack(board, n, row, visited_c, posdiag, negdiag,res):
    if row == n:
        copy =["".join(r) for r in board]
        res.append(copy)
        return
    for c in range(n):
        if c in visited_c or (row+c in posdiag) or (row-c in negdiag):
            continue
        board[row][c] = "Q"
        visited_c.add(c)
        posdiag.add(row+c)
        negdiag.add(row-c)
        backtrack(board, n, row+1, visited_c,posdiag,negdiag,res)
        posdiag.remove(row+c)
        negdiag.remove(row-c)
        visited_c.remove(c)
        board[row][c] = "."

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posdiag = set()
        negdiag = set()
        visited_c = set()

        board = [["."] *n for i in range(n)]
        backtrack(board, n, 0, visited_c, posdiag, negdiag,res)
        return res