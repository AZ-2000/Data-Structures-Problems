# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as queue
def level_order_bfs(q,res):

    while q:
        new_list = []
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            new_list.append(node.val)
        res.append(new_list)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = queue()
        q.append(root)
        res = []
        level_order_bfs(q,res)
        return res        

        
        