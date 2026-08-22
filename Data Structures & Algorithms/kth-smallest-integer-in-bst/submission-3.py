# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder(node, counter, res, k):
    if not node:
        return 
    else:
        inorder(node.left, counter,res,k)
        if counter[0] == k:
            res.append(node.val)
        counter[0] += 1
        print(counter)
        inorder(node.right,counter,res,k)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [1]
        res = []
        inorder(root,counter,res,k)
        return res[0]
        
