from collections import deque as queue
dRow = [1,0,-1,0]
dCol = [0,-1,0,1]

def isValid(grid,r,c, visited):
    return (0<=r<len(grid) and 0<=c<len(grid[r]) and ((r,c) not in visited) and (grid[r][c] != -1) and (grid[r][c] != 0 ))

def bfs_search(grid,q, visited):
    while q:
        cell = q.popleft()
        x = cell[0]
        y = cell[1]

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if not isValid(grid, adjx, adjy, visited):
                continue
            else:
                grid[adjx][adjy] = grid[x][y] + 1 # important point!
                q.append((adjx,adjy))
                visited.add((adjx,adjy))
        

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = queue()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r,c))
        bfs_search(grid,q,visited)
        

                    
        