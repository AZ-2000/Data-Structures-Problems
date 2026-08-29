# def dfs_search(node, word, string, idx):
#     if not node:
#         return
#     if idx == len(word):
#         return True
#     else:
#         if word[idx] in node.children:
#             string[0] += word[idx]
#             idx += 1
#         else:
#             string[0], idx = "", 0
#         dfs_search(node.children, word, idx)
#         string[0] = ""
class SuffixNode:
    def __init__(self):
        self.children = {}
        self.startofword = False
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.suffixroot = SuffixNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True

        word = word[::-1]

        curr = self.suffixroot
        for c in word:
            if c not in curr.children:
                curr.children[c] = SuffixNode()
            curr = curr.children[c]
        curr.startofword = True

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx == len(word):
                return node.endofword

            c = word[idx]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True
                return False
            if c not in node.children:
                return False
            
            return dfs(node.children[c], idx+1)
        return dfs(self.root, 0)


        
