# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def helper(root):
    q = deque()
    output = []
    q.append(root)
    while q:
        tmp_list = []
        node_list = []
        for i in range(len(q)):
            node = q.popleft()
            tmp_list.append(node.val)
            node_list.append(node)

        for item in node_list:
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        output.append(tmp_list)
    
    return output
  
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            return helper(root)

        
        