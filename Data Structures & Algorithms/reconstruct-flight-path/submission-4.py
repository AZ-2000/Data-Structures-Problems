def dfs(adj, source, res):
    while adj[source]:
        neighbour = adj[source].pop()
        dfs(adj, neighbour,res)
    res.append(source)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse = True)
        res = []
        for src, dest in tickets:
            adj[src].append(dest)
        dfs(adj,"JFK", res)
        return res[::-1]
        

