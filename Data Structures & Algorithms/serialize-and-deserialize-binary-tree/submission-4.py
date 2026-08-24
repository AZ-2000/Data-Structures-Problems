# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(node,res):
    if node is None:
        res.append("#,")
        return
    else:
        res.append(str(node.val)+",")
        preorder(node.left,res)
        preorder(node.right,res)

def buildpreorder(ls,idx):
    if idx[0] == len(ls):
        return
    if ls[idx[0]] == "#":
        idx[0] += 1
        return None
    else:
        node = TreeNode(int(ls[idx[0]]))
        idx[0] +=1
        node.left = buildpreorder(ls,idx)
        node.right = buildpreorder(ls,idx)

    return node

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        preorder(root, res)
        word = "".join(res)
        return word
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:  
        ls = [x for x in data.split(',') if x]
        root = buildpreorder(ls, [0])
        return root
             
        