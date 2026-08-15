from collections import deque as queue
def AddCell(grid, r,c,visit,q):
    if (0<=r<len(grid)) and (0<=c<len(grid[0])) and ((r,c) not in visit) and grid[r][c] != 2 and grid[r][c] != 0:
        grid[r][c] = 2
        q.append([r,c])
        visit.add((r,c))
    else:

        return

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = queue()
        visit = set()
        fresh = 0
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[len(grid)-1][len(grid[0])-1] == 0:
                return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2: 
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if not q:
            return -1
        level = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                AddCell(grid, r+1, c, visit,q)
                AddCell(grid, r-1, c, visit,q)
                AddCell(grid, r, c+1, visit,q)
                AddCell(grid, r, c-1, visit,q)
            level += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1: 
                    return -1
        return level-1

        
