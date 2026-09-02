def dfs_directed(adj, source, visited, path, boolean, res):
    path.add(source)
    visited.add(source)

    for i in adj[source]:
        if i not in visited:
            dfs_directed(adj, i, visited, path, boolean, res)
        elif i in path:
            boolean[0] = False
    res.append(source)
    path.remove(source)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        visited = set()
        path = set()
        res = []
        boolean = [True]

        for edge in prerequisites:
            adj[edge[0]].append(edge[1])

        for node in range(numCourses):
            if node not in visited:
                dfs_directed(adj,node,visited,path,boolean,res)
        if not boolean[0]:
            return []
        else:
            return res