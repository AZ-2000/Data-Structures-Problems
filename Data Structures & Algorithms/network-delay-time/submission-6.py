import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for src, destination, weight in times:
            adj[src].append([weight, destination])
        
        source = k
        minheap = [[0, source]]
        visited = set()
        res = 0

        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in visited:
                continue
            for w2, n2 in adj[node]:
                heapq.heappush(minheap, (w2+weight, n2))
            visited.add(node)
            res = weight
        
        if len(visited) != n:
            return - 1
        else:
            return res
            



