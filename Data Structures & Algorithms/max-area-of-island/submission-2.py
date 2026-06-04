class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(row,col):

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return 1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,dfs(i,j))
        
        return maxArea
        