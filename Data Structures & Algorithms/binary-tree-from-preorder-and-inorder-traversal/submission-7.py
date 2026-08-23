# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(idx, preorder, inorder_map,left,right):
    if left > right:
        return
    else:
        node = TreeNode(preorder[idx[0]])
        splitting_point = inorder_map[preorder[idx[0]]]
        idx[0] += 1
        node.left = helper(idx, preorder, inorder_map, left, splitting_point-1)
        node.right = helper(idx, preorder,inorder_map, splitting_point + 1, right)
    return node

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        root = helper([0], preorder, inorder_map, 0, len(inorder)-1)
        return root


