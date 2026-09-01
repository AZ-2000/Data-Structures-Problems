def dfs_directed(adj, visited, source,path, boolean):
    path.add(source)
    visited.add(source)
    for i in adj[source]:
        if i not in visited:
            dfs_directed(adj, visited, i,path, boolean)
        elif i in path:
            boolean[0] = False
    path.remove(source)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()
        adj = defaultdict(list)
        boolean = [True]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        
        for node in list(adj):
            if node not in visited:
                dfs_directed(adj,visited, node,path,boolean)

        return boolean[0]