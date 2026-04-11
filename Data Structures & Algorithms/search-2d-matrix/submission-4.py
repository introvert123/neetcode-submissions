class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1

        row = float('inf')

        while left <= right:
            mid = left + (right-left)//2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break         
            elif target > matrix[mid][n-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            
        if row == float('inf'):
            return False
        
        left = 0
        right = n - 1
        while left <= right:

            mid = left + (right - left)//2

            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
