from collections import deque as queue

dRow = [-1,0,1,0]
dCol = [0,1,0,-1]

def isValid(r,c,grid, visited):
    return((0<=r<len(grid)) and (0<=c<len(grid[r]) or ((r,c) in visited)))

def bfs_multilevel(q, grid,visited):

    while q:
        cell,minute = q.popleft()
        x = cell[0]
        y = cell[1]
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if not isValid(adjx, adjy, grid, visited):
                continue
            if grid[adjx][adjy] != 1:
                continue
            else:
                visited.add((adjx,adjy))
                q.append(((adjx,adjy), minute + 1))
                grid[adjx][adjy] = 2

    return minute

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = queue()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append(((r,c),0))
        if not q:
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 1:
                        return -1
            return 0
        minutes = bfs_multilevel(q, grid, visited)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        return minutes