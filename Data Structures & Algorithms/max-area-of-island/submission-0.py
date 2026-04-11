class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        directions = [[0,-1], [0,1], [1,0], [-1,0]]

        def dfs(r,c):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == 0 or 
                (r, c) in visited):
                return 0

            visited.add((r, c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area



        for row in range(rows):
            for col in range(cols):
                # the reason why we use visited is bcoz we do not want to go through
                # the same item which is part of the island we visited already
                if grid[row][col] == 1 and (row,col) not in visited:
                    maxArea = max(dfs(row, col), maxArea)
        
        return maxArea
        

