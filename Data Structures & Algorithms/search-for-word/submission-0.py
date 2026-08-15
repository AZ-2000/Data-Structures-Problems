def helper(row, col, idx, board, word, visited):
    if idx == len(word):
        return True
    if (row<0 or col<0 or row>= len(board) or col >= len(board[0]) or word[idx] != board[row][col] or (row,col) in visited):
        return False
    

    visited.add((row,col))
    res = (helper(row+1,col, idx+1, board,word, visited) or helper(row, col+1, idx+1, board,word,visited)
    or helper(row-1, col, idx+1, board, word, visited) or helper(row, col-1, idx+1, board, word,visited))
    visited.remove((row,col))
    return res




class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if helper(row, col, 0, board, word,visited):
                    return True
        return False
        