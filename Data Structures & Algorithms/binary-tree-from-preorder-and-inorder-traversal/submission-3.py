# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(preorder, inorder_map, pre_idx, left, right):
    if left > right:
        return None
    root_val = preorder[pre_idx[0]]
    pre_idx[0] += 1
    root = TreeNode(root_val)
    mid = inorder_map[root_val]
    root.left = dfs(preorder, inorder_map, pre_idx, left, mid-1)
    root.right = dfs(preorder, inorder_map, pre_idx, mid + 1, right)
    return root

    
    



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val: i for i, val in enumerate(inorder)}
        return dfs(preorder, inorder_map, [0],0, len(inorder)-1)


