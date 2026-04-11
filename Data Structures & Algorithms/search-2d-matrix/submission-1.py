class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        # binary search to find the correct row in which we have to do the binary search
        top = 0
        bot = m - 1
        mid = 0
        while top<=bot:
            mid = (top + bot)//2
            if target > matrix[mid][n-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        # binary search in the found row
        row = mid
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
        