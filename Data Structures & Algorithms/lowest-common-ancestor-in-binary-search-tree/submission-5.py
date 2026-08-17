# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def searchBST(node, maxima):
    if not node:
        return False
    else:
        if node.val < maxima:
           return searchBST(node.right, maxima)
        elif node.val > maxima:
           return searchBST(node.left,maxima)
        else:
            return True
    
def LCA_func(node, minima, maxima, LCA):
    if not node:
        return 
    else:

        if node.val == minima.val or node.val == maxima.val:
            if node.val == minima.val:
                if searchBST(node,maxima.val):
                    LCA[0] = minima.val
                    LCA[1] = minima
            elif node.val == maxima.val:
                if searchBST(node, minima.val):
                    LCA[0] = maxima.val
                    LCA[1] = maxima

        if node.val > minima.val and node.val < maxima.val and not LCA[1]:
            LCA[0] = node.val
            LCA[1] = node

        LCA_func(node.left, minima,maxima, LCA)
        LCA_func(node.right, minima,maxima, LCA)
        
    
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < q.val:
            minima = p
            maxima = q
        else:
            minima = q
            maxima = p
        
        LCA =[float('infinity'),None]

        LCA_func(root, minima,maxima, LCA)
        return LCA[1]