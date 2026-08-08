class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        while l <= r:
            mid_1 = (r+l)//2
            if matrix[mid_1][len(matrix[mid_1])-1] < target:
                l = mid_1 + 1
                # print(matrix[mid_1][len(matrix[mid_1])-1])
            elif matrix[mid_1][0] > target:
                r = mid_1 - 1
                # print(matrix[mid_1][len(matrix[mid_1])-1])                
            else:
                ls = matrix[mid_1]
                i, j = 0, len(ls)-1
                while i <= j:
                    mid_2 = (i+j) // 2
                    if ls[mid_2] < target:
                        i = mid_2 + 1
                    elif ls[mid_2] > target:
                        j = mid_2 - 1
                    else:
                        return True
                return False
        return False

