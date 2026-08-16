def dfs(node, adj, visited):
    visited.add(node)
    for neighbor in adj[node]:
        if neighbor not in visited:
            dfs(neighbor, adj, visited)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = set()
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            
            adj[u].append(v)
            adj[v].append(u)

        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node, adj, visited)

        return components
        
