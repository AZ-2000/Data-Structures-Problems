class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pos = []
        subgrid_size = 3
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != ".":
                    pos.append([board[row][col], row, col, row//subgrid_size, col//subgrid_size])
                else:
                    continue
        print(pos)
        for i in range(len(pos)):
            j = i + 1
            while j < len(pos):
                if pos[i][0] == pos [j][0]:
                    if pos[i][3] == pos[j][3] and pos[i][4] == pos[j][4]:
                        return False
                    if pos[i][1] - pos[j][1] == 0:
                        return False
                    if pos[i][2] - pos[j][2] == 0:
                        return False
                j += 1
        return True
 

        

                



        