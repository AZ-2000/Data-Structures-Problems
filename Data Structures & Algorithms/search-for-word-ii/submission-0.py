class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def AddWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.endofword = True

    def pruneWord(self, word):
        curr = self.root
        nodeandchildkey = []

        for c in word:
            nodeandchildkey.append((curr, c))
            curr = curr.children[c]

        for parentnode, childkey in reversed(nodeandchildkey):
            targetnode = parentnode.children[childkey]

            if len(targetnode.children) == 0:
                del parentnode.children[childkey]
            else:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Trie()

        for w in words:
            root.AddWord(w)

        rows, cols = len(board), len(board[0])
        res = []
        visit = set()

        def dfs(r, c, node, word):

            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or board[r][c] not in node.children
                or (r, c) in visit
            ):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endofword:
                res.append(word)
                node.endofword = False
                root.pruneWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root.root, "")

        return res