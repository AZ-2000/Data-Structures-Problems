class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixmatrix = [[0] * (len(matrix[0])) for _ in range(len(matrix) )]
        summa = matrix[0][0]
        for c in range(len(matrix[0])):
            self.prefixmatrix[0][c] = summa
            if c < len(matrix[0])-1:
                summa += matrix[0][c+1]
        summa = matrix[0][0]
        for r in range(len(matrix)):
            self.prefixmatrix[r][0] = summa
            if r < len(matrix)-1:
                summa += matrix[r+1][0]

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                self.prefixmatrix[r][c] = self.prefixmatrix[r-1][c] + self.prefixmatrix[r][c-1] + matrix[r][c] - self.prefixmatrix[r-1][c-1]
        
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefixmatrix[row2][col2]
        if row1 > 0:
            total -= self.prefixmatrix[row1-1][col2]
        if col1 > 0:
            total -= self.prefixmatrix[row2][col1-1]
        
        if row1 > 0 and col1 > 0:
            total += self.prefixmatrix[row1 -1][col1-1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)