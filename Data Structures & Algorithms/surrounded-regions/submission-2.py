from collections import deque as queue

dRow = [-1,0,1,0]
dCol = [0,1,0,-1]

def isValid(grid, r,c):
    return((0<=r<len(grid)) and (0<=c<len(grid[r])))

def multilevelbfs(grid,q, untouchables):
    while q:
        for i in range(len(q)):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]
            for j in range(4):
                adjx = x + dRow[j]
                adjy = y + dCol[j]
                if not isValid(grid,adjx,adjy):
                    continue
                else:
                    if grid[adjx][adjy] == "O" and ((adjx, adjy) not in untouchables):
                        untouchables.add((adjx,adjy))
                        q.append((adjx,adjy))
                    else:
                        continue
                    

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()
        q = queue()

        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or r == len(board) - 1:
                    if board[r][c] == "O":
                        border.add((r,c))
                        q.append((r,c))
                if c == 0 or c == len(board[r]) - 1:
                    if board[r][c] == "O":
                        border.add((r,c))
                        q.append((r,c))
        multilevelbfs(board,q,border)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if ((r,c)) not in border:
                    board[r][c] = "X"

        
        
