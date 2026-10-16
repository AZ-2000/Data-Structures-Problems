dRow = [1,0,-1,0]
dCol = [0,1,0,-1]
def isValid(board, r, c, visited):
    if 0<=r<len(board) and 0<=c<len(board[r]) and (r,c) not in visited:
        return True
    else:
        return False

def backtrack_dfs(board, word, idx,r,c, curr, res, visited):
    if idx == len(word):
        print("".join(curr))
        res[0] = True
        return 
    else:
        # print(isValid(board, r, c, visited), r,c, visited)
        if isValid(board, r, c, visited) and word[idx] == board[r][c]:
            # print( r, c, "".join(curr), board[r][c], word[idx])
            curr.append(word[idx])
            visited.add((r,c))
            for i in range(4):
                adjx = r + dRow[i]
                adjy = c + dCol[i]
                backtrack_dfs(board, word, idx+1, adjx,adjy, curr, res, visited)
            visited.remove((r,c))
            curr.pop()
        else:
            return

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = [False]
        curr = []
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if word[0] == board[r][c]:
                    backtrack_dfs(board, word, 0, r, c, curr, res, visited)
                    if res[0]:
                        return res[0]
        return res[0]


        


        
        