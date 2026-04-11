class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()
        res = []

        def dfs(row,col,visit,prevHeight):

            if row < 0 or col < 0 or row == rows or col == cols or (row,col) in visit or heights[row][col] < prevHeight:
                return 

            visit.add((row,col))
            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col])
            dfs(row,col-1,visit,heights[row][col])
            dfs(row,col+1,visit,heights[row][col])

        #from top and bottom - we do dfs to find out what all cells can flow into pacific or atlantic
        for col in range(cols):
            dfs(0,col,pac,heights[0][col])
            dfs(rows-1,col,atl,heights[rows-1][col])

        #from left and right - we do dfs to find out what all cells can flow into pacific or atlantic
        for row in range(rows):
            dfs(row,0,pac,heights[row][0])
            dfs(row,cols-1,atl,heights[row][cols-1])

        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    res.append([row,col])
        
        return res


