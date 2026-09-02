def dfs_graph(adj, visited, parent, source, target):
    if source == target:
        return True
    
    visited.add(source)
    for node in adj[source]:
        if node == parent:
            continue
        if node not in visited:
            if dfs_graph(adj, visited,source,node, target):
                return True
    return False
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u,v in edges:
            visited = set()
            if dfs_graph(adj, visited, -1, u, v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)