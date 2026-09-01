from collections import deque as queue
dRow = [-1,0,1,0]
dCol = [0,1,0,-1]
def isValid(grid,r, c, visited):
    return ((0<=r<len(grid)) and (0<=c<len(grid[r]) and ((r,c) not in visited)))


def bfs_multilevel(grid, q, atlantic, pacific, visited):
    while q:
        for i in range(len(q)):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if not isValid(grid, adjx, adjy, visited):
                    continue
                elif grid[x][y] <= grid[adjx][adjy]:
                    if ((x,y)) in atlantic:
                        if ((adjx,adjy)) not in atlantic:
                            atlantic.add((adjx,adjy))
                            q.append((adjx,adjy))
                    if ((x,y)) in pacific:
                        if ((adjx,adjy)) not in pacific:
                            pacific.add((adjx,adjy))
                            q.append((adjx,adjy))
                    
                else:
                    continue
        

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        visited = set()
        q = queue()

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if row == 0:
                    pacific.add((row,col))
                    q.append((row,col))
                if row == len(heights)-1:
                    atlantic.add((row,col))
                    q.append((row,col))
                if col == 0:
                    pacific.add((row,col))
                    q.append((row,col))
                if col == len(heights[row]) - 1:
                    atlantic.add((row,col))
                    q.append((row,col))
        res = []
        bfs_multilevel(heights, q, atlantic, pacific, visited)

        for item in atlantic:       
            if item in pacific:
                res.append(list(item))
        return res