# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder_serialize(node,res):
    if not node:
        res.append("#,")
    else:
        res.append(str(node.val)+',')
        preorder_serialize(node.left,res)
        preorder_serialize(node.right,res)
    
def helper(vals, idx):
    if idx[0] >= len(vals):
        return None

    if vals[idx[0]] == None:
        idx[0] += 1
        return None

    node = TreeNode(int(vals[idx[0]]))
    idx[0] += 1

    node.left = helper(vals, idx)
    node.right = helper(vals, idx)

    return node
        
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        preorder_serialize(root, res)
        word = "".join(map(str, res))
        return word
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:        
        ls = []
        empty = ""
        idx = [0]
        for i in range(len(data)):
            if not data[i] == ",":
                empty += data[i]
            elif data[i] == ",":
                ls.append(empty)
                empty = ""
        for i in range(len(ls)):
            if ls[i] != "#":
                ls[i] = int(ls[i])
            elif ls[i] == "#":
                ls[i] = None
        root = helper(ls, idx)
        return root
