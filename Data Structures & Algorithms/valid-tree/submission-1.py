def dfs(adj, node, visited,parent):
    visited.add(node)

    for neighbor in adj[node]:
        if neighbor == parent:
            continue

        if neighbor in visited:
            return False
        if not dfs(adj, neighbor, visited, node):
            return False

    return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[]for i in range(n)]
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                if components > 1:
                    return False
                if not dfs(adj, i, visited, -1):
                    return False
        return True
            
            

        
        
