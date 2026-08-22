# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(node):
    if not node:
        return 0
    else:
        left = height(node.left)
        right = height(node.right)
    
    return 1 + max(left, right)

def isBalanced(node, flag):
    if not node:
        return 
    else:
        left = isBalanced(node.left, flag)
        right = isBalanced(node.right, flag)
        h_left = height(left)
        h_right = height(right)
        if abs(h_right - h_left) > 1:
            print('here', h_right, h_left)
            print(flag[0])
            flag[0] = False
    return node
        

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        isBalanced(root, flag)
        return flag[0]

        