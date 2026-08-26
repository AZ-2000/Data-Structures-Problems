def backtrack(board, word, idx, row, col,res, seen):
    if not idx < len(word) or not(0<=row<len(board)) or not(0<=col<len(board[0])) or (row,col) in seen:

        return False
    seen.add((row,col))
    res.append(board[row][col])
    if word == "".join(res):
        return True

    boolean =  (backtrack(board,word, idx+1, row + 1, col, res, seen) or backtrack(board, word, idx+1, row, col+1, res,seen) or backtrack(board,word, idx+1, row-1, col, res, seen) or backtrack(board,word, idx+1, row, col-1, res, seen))
    seen.remove((row, col))
    res.pop()
    return boolean

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):        
                if backtrack(board, word, 0, row,col,res, seen):
                    return True
        return False
        


        
        