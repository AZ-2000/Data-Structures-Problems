import heapq

dRow = [1,0,-1,0]
dCol = [0,1,0,-1]

def isValid(grid, r,c,visited):
    return((0<=r<len(grid)) and(0<=c<len(grid[r])) and ((r,c) not in visited))

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = []
        heapq.heappush(minheap,(grid[0][0], 0, 0))
        visited = set()
        visited.add((0,0))
        max_elevation = 0
        while minheap:
            elevation, x,y = heapq.heappop(minheap)
            if x == len(grid) - 1 and y == len(grid[x]) - 1:
                return elevation
            else:
                max_elevation = elevation
                for i in range(4):
                    adjx = x + dRow[i]
                    adjy = y + dCol[i]
                    if not isValid(grid, adjx, adjy, visited):
                        continue
                    else:
                        visited.add((adjx,adjy))
                        heapq.heappush(minheap, [max(grid[adjx][adjy], max_elevation), adjx, adjy])
