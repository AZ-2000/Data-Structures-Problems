def dfs_backtrack(grid, num_queens, res, posdiag, negdiag,r, rank, file):
    if num_queens == len(grid):
        res.append(["".join(row) for row in grid])
    else:
        for c in range(len(grid)):
            if (r+c) not in posdiag and r-c not in negdiag and r not in rank and c not in file:
                grid[r][c] = "Q"
                posdiag.add(r+c)
                negdiag.add(r-c)
                rank.add(r)
                file.add(c)
                dfs_backtrack(grid, num_queens + 1, res, posdiag, negdiag, r+1,rank, file)
                grid[r][c] = "."
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                rank.remove(r)
                file.remove(c)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for i in range(n)] for _ in range(n)]
        pos_diag = set()
        neg_diag = set()
        rank = set()
        file = set()
        res = []

        dfs_backtrack(grid, 0, res, pos_diag, neg_diag, 0, rank, file )
        print(res)
        return res