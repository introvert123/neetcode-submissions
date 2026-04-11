class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r,c):

            if grid[r][c] == "1":
                visited.add((r,c))
            else:
                return

            for dr,dc in directions:
                row = r + dr
                col = c + dc
                if row in range(rows) and col in range(cols) and (row,col) not in visited:
                    dfs(row,col)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands

        