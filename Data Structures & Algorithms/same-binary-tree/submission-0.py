# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node,res):
        if not node:
            res.append(None)
        else:
            res.append(node.val)
            self.dfs(node.left,res)
            self.dfs(node.right,res)
        return res

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        new_res = self.dfs(p,res1)
        new_res_2 = self.dfs(q,res2)
        
        if len(new_res) != len(new_res_2):
            return False

        else:
            for i in range(len(new_res)):
                if new_res[i] != new_res_2[i]:
                    return False

            return True

        


