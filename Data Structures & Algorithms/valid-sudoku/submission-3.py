class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) #represents all values in the col
        rows = collections.defaultdict(set) #represents all values in the rows
        squares = collections.defaultdict(set) #represents sub boxes

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])

                squares[(r//3,c//3)].add(board[r][c])
        return True


        