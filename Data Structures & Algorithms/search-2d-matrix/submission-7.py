class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row_length = len(matrix) - 1
        col_length = len(matrix[0]) - 1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[mid][col_length]:
                l = mid + 1
            elif target < matrix[mid][col_length]:
                l_2, r_2 = 0, col_length
                while l_2 < r_2:
                    mid_2 = (l_2+r_2)//2
                    if target < matrix[mid][mid_2]:
                        r_2 = mid_2 
                    if target > matrix[mid][mid_2]:
                        l_2 = mid_2 +1
                    elif target == matrix[mid][mid_2]:
                        return True
                r = mid - 1
            elif target == matrix[mid][col_length]:
                return True
        return False


