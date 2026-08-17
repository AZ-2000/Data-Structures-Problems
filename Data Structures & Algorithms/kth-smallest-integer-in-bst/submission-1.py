# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(node,k, target,node_val):
    if not node:
        return 
    else:
        inorder(node.left,k, target, node_val)
        k[0] += 1
        if k[0] == target:
            node_val[0] = node.val
        inorder(node.right,k, target, node_val)
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]
        node_val = [0]
        inorder(root, counter, k, node_val)
        return node_val[0]
        
