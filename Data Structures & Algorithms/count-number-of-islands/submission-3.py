class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row,col):

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return 

            grid[row][col] = "0"

            dfs(row-1, col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            return


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "0":
                    dfs(i,j)
                    islands = islands + 1

        
        return islands
                    



        