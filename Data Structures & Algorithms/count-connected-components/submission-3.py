from collections import deque as queue

def bfs_adj_list(adj_list, visited,start):
    q = queue()
    q.append(start)
    visited.add(start)
    while q:
        neighbours = q.popleft()
        for n in adj_list[neighbours]:
            if n not in visited:
                visited.add(n)
                q.append(n)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visited = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        components = 0
        for node in range (n):
            if node not in visited:
                components += 1
                bfs_adj_list(adj_list, visited, node)
        return components

        
