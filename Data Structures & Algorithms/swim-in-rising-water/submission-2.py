import heapq
dRow = [1,0,-1,0]
dCol = [0,1,0,-1]
def isValid(grid, r, c, visited):
    return (0<=r<len(grid) and (0<=c<len(grid[r]) and ((r,c) not in visited)))

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minheap = [[grid[0][0],0,0]]
        visited.add((0,0))
        while minheap:
            cell = heapq.heappop(minheap)
            time, row, col = cell[0],cell[1],cell[2]

            if row == len(grid)-1 and col == len(grid[row])-1:
                return time
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                if not isValid(grid, adjx,adjy,visited):
                    continue
                visited.add((adjx,adjy))
                heapq.heappush(minheap,[max(time, grid[adjx][adjy]),adjx,adjy])
                

