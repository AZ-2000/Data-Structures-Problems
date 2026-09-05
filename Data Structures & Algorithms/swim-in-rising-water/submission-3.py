import heapq

dRow = [1,0,-1,0]
dCol = [0,1,0,-1]

def isValid(grid, r,c,visited):
    return (0<=r<len(grid) and (0<=c<len(grid[r])) and ((r,c) not in visited))

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [[grid[0][0], 0, 0]]
        visited = set()
        visited.add((0,0))
        while minheap:
            time, x, y = heapq.heappop(minheap)
            if x == len(grid)-1 and y == len(grid[x]) -1:
                return time

            for i in range(4):
                adjx = dRow[i] + x
                adjy = dCol[i] + y
                if not isValid(grid,adjx,adjy,visited):
                    continue
                else:
                    visited.add((adjx,adjy))
                    heapq.heappush(minheap,[max(time,grid[adjx][adjy]), adjx,adjy])



        