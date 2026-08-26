def backtrack(row, col, board, word, idx, res, seen):
    if idx == len(word):
        return True
    if not(0<=row<len(board)) or not(0<=col<len(board[0])) or (row,col) in seen:
        return False
    if board[row][col] != word[idx]:
        return False

    seen.add((row,col))
    res.append(board[row][col])
    idx += 1
    
    boolean = (backtrack(row+1,col, board, word, idx, res, seen) or 
    backtrack(row-1, col, board, word, idx, res, seen) or backtrack(row,
    col+1, board, word, idx, res, seen) or backtrack(row, col-1, board, word, idx, res, seen))
    res.pop()
    seen.remove((row,col))
    return boolean

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, board, word, 0, res, seen):
                    return True
        return False
        
        


        
        