def backtrack(n, num_queens,r,posdiag, negdiag, rank, file, sol):
    if num_queens == n:
        sol[0] += 1
        return
    for c in range(n):
        if (r+c) not in posdiag and (r-c) not in negdiag and r not in rank and c not in file:
            posdiag.add(r+c)
            negdiag.add(r-c)
            rank.add(r)
            file.add(c)
            backtrack(n, num_queens+1, r+1, posdiag, negdiag, rank,file,sol)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            rank.remove(r)
            file.remove(c)

class Solution:
    def totalNQueens(self, n: int) -> int:
        # grid = [['.' for _ in range(n)] for _ in range(n)]
        sol = [0]
        posdiag = set()
        negdiag = set()
        rank = set()
        file = set()
        backtrack(n, 0, 0, posdiag, negdiag, rank, file, sol)
        return sol[0]

        
        