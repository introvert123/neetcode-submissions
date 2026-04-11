class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1], [1,0],[0,-1],[-1,0]]
        minutes = 0
        fresh = 0

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1

        while queue and fresh > 0:
            size = len(queue)
            
            for i in range(size):
                (r,c) = queue.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row,col))
                        fresh -= 1
            
            minutes += 1

        return minutes if fresh == 0 else -1
        