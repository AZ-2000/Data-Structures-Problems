import heapq

def calc_manhattan(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = calc_manhattan(points[i], points[j])
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res = 0
        visited = set()
        minheap = [[0,0]]

        while len(visited) < len(points):
            cost, pt = heapq.heappop(minheap)
            if pt in visited:
                continue
            res += cost
            visited.add(pt)
            for neighbour_cost, neighbour in adj[pt]:
                if neighbour not in visited:
                    heapq.heappush(minheap,[neighbour_cost, neighbour])
        return res

        
        

        
        
