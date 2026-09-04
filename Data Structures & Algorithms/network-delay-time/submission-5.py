import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for source, destination, weight in times:
            adj[source].append([weight,destination])
        
        res = 0
        source = k
        visited = set()
        minheap= []
        heapq.heappush(minheap, (0,k))

        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in visited:
                continue
            else:
                for w, neighbour in adj[node]:
                    heapq.heappush(minheap,(w + weight, neighbour))
                res = weight
                visited.add(node)
        if len(visited) != n:
            return -1
        else:
            return res


