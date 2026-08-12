# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
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

            output.append(tmp_list[-1])
        
        return output