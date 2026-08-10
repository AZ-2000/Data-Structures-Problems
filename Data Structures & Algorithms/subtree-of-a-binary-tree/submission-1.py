# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder_dfs(node, res):
    if not node: 
        res.append(None)
    else:
        res.append(node.val)
        preorder_dfs(node.left, res)
        preorder_dfs(node.right,res)
    
    return res



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = []
        sub_res = []
        res = preorder_dfs(root,res)
        sub_res = preorder_dfs(subRoot, sub_res)
        n = len(sub_res)

        return any(res[i:i+n] == sub_res for i in range(len(res)-n + 1))
        