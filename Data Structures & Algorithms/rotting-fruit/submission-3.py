class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        minutes = 0

        def rot(row,col):

            if row >= 0 and row < rows and col >=0 and col < cols and grid[row][col] == 1:
                grid[row][col] = 2
                queue.append([row,col])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])


        while queue:
            size = len(queue)
            for i in range(size):
                (row,col) = queue.popleft()
                rot(row+1,col)
                rot(row-1,col)
                rot(row,col+1)
                rot(row,col-1)
            if len(queue) != 0:
                minutes += 1  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minutes

        