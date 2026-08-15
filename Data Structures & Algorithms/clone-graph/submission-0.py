"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
def dfs(node, hashmap):
    if node in hashmap:
        return hashmap[node]
    copy = Node(node.val)
    hashmap[node] = copy
    for neighbor in node.neighbors:
        copy.neighbors.append(dfs(neighbor,hashmap))
    return copy

 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        if not node:
            return None
        return dfs(node, hashmap)

        