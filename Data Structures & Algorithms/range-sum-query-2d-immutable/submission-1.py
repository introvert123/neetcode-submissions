class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.sumMat = [[0]*(cols+1) for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]

                above = self.sumMat[r-1][c]
                self.sumMat[r][c] = prefix + above
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:

        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        aboveLeft = self.sumMat[r1-1][c1-1]

        return bottomRight - above - left + aboveLeft

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)