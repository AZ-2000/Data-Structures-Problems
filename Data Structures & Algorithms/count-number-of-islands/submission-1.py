from collections import deque as queue

dRow = [-1,0,1,0]
dCol = [0,1,0,-1]

def isSafe(grid, r, c,vis):
    rows = len(grid)
    cols = len(grid[0])
    return (0<=r<rows) and (0<=c<cols) and grid[r][c] == '1' and (r,c) not in vis
def bfs_matrix(grid, vis, r,c):
    q = queue()
    q.append((r,c))
    vis.add((r,c))
    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isSafe(grid, adjx, adjy, vis):
                q.append((adjx, adjy))
                vis.add((adjx,adjy))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        vis = set()
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in vis:
                    bfs_matrix(grid,vis,r, c)
                    island_count +=1
        return island_count
        