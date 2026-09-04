import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for source, destination, weight in times:
            adj[source].append([weight, destination])
        
        source = k
        shortest = {}

        minheap = [[0,k]]

        while minheap:
            weight, source = heapq.heappop(minheap)
            if source in shortest:
                continue
            for w2, src in adj[source]:
                heapq.heappush(minheap, (w2+weight, src))
            shortest[source] = weight

        if len(shortest) != n:
            return -1

        
        return max(shortest.values())


