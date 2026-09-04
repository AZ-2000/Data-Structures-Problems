import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for source, destination, weight in times:
            adj[source].append([weight, destination])
        
        source = 1
        shortest = {}
        minheap = [[0,k]]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            else:
                shortest[n1] = w1
                for node in adj[n1]:
                    node[0] += w1
                    heapq.heappush(minheap, node)
        
        if len(shortest) != n:
            return -1
        return max(shortest.values())