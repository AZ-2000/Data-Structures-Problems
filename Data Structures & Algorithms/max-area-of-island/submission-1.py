from collections import deque as queue

dRow = [-1,0,1,0]
dCol = [0,1,0,-1]

def isSafe(grid,r,c,vis):
    rows = len(grid)
    cols = len(grid[0])
    return (0<=r<rows) and (0<=c<cols) and (grid[r][c]==1 and not 
    vis[r][c])

def bfs_matrix(grid, r,c,vis,maxarea):
    q = queue()
    area = 0
    q.append((r,c))
    vis[r][c] = True

    while q:
        cell = q.popleft()
        area += 1
        x = cell[0]
        y = cell[1]
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isSafe(grid, adjx, adjy, vis):
                q.append((adjx,adjy))
                vis[adjx][adjy] = True

    maxarea[0] = max(area, maxarea[0])
        

    

def Island_Count(grid):
    rows = len(grid)
    cols = len(grid[0])
    maxarea = [0]
    vis =[[False] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not vis[r][c]:
                bfs_matrix(grid,r,c,vis,maxarea)
    return maxarea[0]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return Island_Count(grid)
        