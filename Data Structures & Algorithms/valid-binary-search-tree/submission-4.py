# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(node, res):
    if node is None:
        return
    else:
        inorder(node.left,res)
        res.append(node.val)
        inorder(node.right,res)
    return res

    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        res = inorder(root,res)
        if len(res) == 2:
            if res[0] >= res[1]:
                return False
        for i in range(len(res)):
            # print(res)
            if 1 <= i <= len(res) - 2:
                if not (res[i-1] < res[i] < res[i+1]):
                    print(res[i-1], res[i], res[i+1])
                    return False
        return True


        
        