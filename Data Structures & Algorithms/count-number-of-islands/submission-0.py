from collections import deque as queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def isSafe(grid, r, c, vis):
    rows = len(grid)
    cols = len(grid[0])

    return (0<=r<rows) and (0<=c<cols) and (grid[r][c] == '1'
    and not vis[r][c])

def bfs_matrix(grid, vis, row, col):
    q = queue()
    q.append((row,col))
    vis[row][col] = True
    while q:
        cell = q.popleft()

        x = cell[0]
        y = cell[1]

        for i in range(4):
            adjx = x+dRow[i]
            adjy = y + dCol[i]
            if isSafe(grid,adjx,adjy,vis):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True

def Island_Count(grid):
    rows = len(grid)
    cols = len(grid[0])
    vis = [[False] * cols for _ in range(rows)]
    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not vis[r][c]:
                bfs_matrix(grid, vis, r,c)
                island_count += 1
    return island_count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return Island_Count(grid)
        