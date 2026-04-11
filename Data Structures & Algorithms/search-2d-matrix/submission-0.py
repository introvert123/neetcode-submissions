class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        while i < m:
            if target > matrix[i][n-1]:
                i = i + 1
            else:
                row = i
                right = n - 1
                col = 0
                while col<=right:
                    mid = col + (right - col)//2
                    if target == matrix[row][mid]:
                        return True
                    elif target > matrix[row][mid]:
                        col = mid + 1
                    else:
                        right = mid - 1
                
                return False

        
        return False
        