def dfs(v, adj, visited, parent):
    visited[v] = True

    for neighbour in adj[v]:
        if not visited[neighbour]:
            if dfs(neighbour, adj, visited, v):
                return True
        elif neighbour != parent:
            return True
    return False

def isCycle(adj):
    V = len(adj)
    visited = [False] * V

    for u in range(V):
        if not visited[u]:
            if dfs(u, adj, visited, -1):
                return True
    return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return not isCycle(adj)
        
