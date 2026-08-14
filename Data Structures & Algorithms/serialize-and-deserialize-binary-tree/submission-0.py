# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(node,res):
    if not node:
        res.append("N#")
    else:
        res.append(str(node.val) + "#")
        preorder(node.left, res)
        preorder(node.right, res)
def helper(vals):
    val = next(vals)
    if val == "N":
        return None
    node = TreeNode(int(val))
    node.left = helper(vals)
    node.right = helper(vals)

    return node
    


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        preorder(root, res)
        res = "".join(str(x) for x in res)
        return res
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split("#"))
        root = helper(vals)
        return root
        



