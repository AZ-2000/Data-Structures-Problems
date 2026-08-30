from collections import deque as queue
drow = [0,1,0,-1]
dcol = [1,0,-1,0]

def isValid(r,c,grid, visit):
    return ((0<=r<len(grid)) and (0<=c<len(grid[0])) and ((r,c) not in visit) and grid[r][c] != 0)

def search(grid,r,c, visited):
    maxarea = 0
    q = queue()
    q.append((r,c))
    visited.add((r,c))
    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        for i in range(4):
            adjx = x + drow[i]
            adjy = y + dcol[i]
            if isValid(adjx, adjy, grid, visited):
                q.append((adjx, adjy))
                maxarea += 1
            visited.add((adjx, adjy))

    return maxarea + 1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        maximumarea = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r,c) not in visited:
                    maximumarea = max(maximumarea, search(grid,r,c,visited))
        return maximumarea


                
        