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
    else:
        new_node = Node(node.val)
        hashmap[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(dfs(neighbor, hashmap))
        
        return new_node
            
 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        hashmap = {}
        cloned_node = dfs(node, hashmap)
        return cloned_node

        