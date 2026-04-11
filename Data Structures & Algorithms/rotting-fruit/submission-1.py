class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[0,1], [1,0],[0,-1],[-1,0]]
        minutes = 0

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2 and (row,col) not in visited:
                    queue.append((row,col))


        while queue:
            size = len(queue)
            

            for i in range(size):
                (r,c) = queue.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row,col) not in visited:
                        grid[row][col] = 2
                        queue.append((row,col))
                        visited.add((row,col))
            
            if len(queue) != 0:
                minutes += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return minutes
        