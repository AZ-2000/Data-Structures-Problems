import heapq

def calc_manhattan_dist(p1,p2):
    dist = abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
    return dist

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = calc_manhattan_dist(points[i], points[j])
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        res = 0
        visited = set()
        minheap = [[0,0]]
        while len(visited) < N:
            cost,point = heapq.heappop(minheap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for neicost, neighbour in adj[point]:
                if neighbour not in visited:
                    heapq.heappush(minheap, [neicost, neighbour])
        return res
        


            

