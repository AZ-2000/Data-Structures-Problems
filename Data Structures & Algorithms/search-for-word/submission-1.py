def helper(row, col, board, word, curr, visited):
    if not (0<=row<len(board)) or not(0<=col<len(board[0])) or ((row,col) in visited) or (len(curr) >= len(word) and curr != word):
        return False
    else:
        visited.add((row,col))
        curr += board[row][col]
        print(curr)
        if curr == word:
            return True
    
        res = (helper(row+1, col, board,word, curr, visited)or
        helper(row, col-1, board,word, curr, visited)or
        helper(row-1, col, board,word, curr, visited)or
        helper(row, col + 1, board,word, curr, visited))
        visited.remove((row,col))
        return res

        # return(helper(row+1, col, board,word, word_idx, curr, visited)or
        # helper(row, col-1, board,word, word_idx, curr, visited)or
        # helper(row-1, col, board,word, word_idx, curr, visited)or
        # helper(row, col + 1, board,word, word_idx, curr, visited))
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curr = ""
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(row, col, board, word,curr, visited):
                    return True
        return False
        