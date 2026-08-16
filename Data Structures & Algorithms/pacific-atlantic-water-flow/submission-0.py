def setadjacent(r,c,heights, adjlist):
    if 0<=r+1<len(heights):
        adjlist[(r+1,c)] = heights[r+1][c]
    if r - 1>= 0:
        adjlist[(r-1,c)] = heights[r-1][c]
    if 0<= c + 1 < len(heights[0]):
        adjlist[(r,c+1)] = heights[r][c+1]
    if c -1 >= 0:
        adjlist[(r,c-1)] = heights[r][c-1]


def dfs(r,c,heights,pacific, atlantic, visited_atlantic, visited_pacific):
    if not (0<=r<len(heights)) or not (0<=c<len(heights[0])):
        return 
    if (r,c) in atlantic:
        visited_atlantic.add((r,c))

    if (r,c) in pacific:
        visited_pacific.add((r,c))

    adjlist = {}
    setadjacent(r,c,heights,adjlist)
    for k, v in adjlist.items():
        if (r,c) in atlantic and k not in visited_atlantic:
            if heights[r][c] <= v:
                atlantic[k] = heights[r][c]
                new_r,new_c = k
                visited_atlantic.add(k)
                dfs(new_r, new_c, heights, pacific, atlantic, visited_atlantic, visited_pacific)
        if (r,c) in pacific and k not in visited_pacific:
            if heights[r][c] <= v:
                pacific[k] = heights[r][c]
                new_r,new_c = k
                visited_pacific.add(k)
                dfs(new_r, new_c, heights, pacific, atlantic, visited_atlantic, visited_pacific)
            

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = {}
        atlantic = {}
        res = []
        visited_pacific = set()
        visited_atlantic = set()

        for row in range(len(heights)): 
            for col in range(len(heights[0])): 
                if row == 0: 
                    pacific[(row,col)] = True 
                if row == len(heights) - 1:
                    atlantic[(row,col)] = True 
                if col == (len(heights[0])-1): 
                    atlantic[(row,col)] = True 
                if col == 0:
                    pacific[(row,col)] = True
        
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0:
                    dfs(row,col, heights, pacific, atlantic, visited_atlantic, visited_pacific)
                if row == len(heights)-1:
                    dfs(row,col, heights, pacific, atlantic, visited_atlantic, visited_pacific)
                if col == len(heights[0]) -1:
                    dfs(row,col, heights, pacific, atlantic, visited_atlantic, visited_pacific)
                if col == 0:
                    dfs(row,col, heights, pacific, atlantic, visited_atlantic, visited_pacific)
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        return res



