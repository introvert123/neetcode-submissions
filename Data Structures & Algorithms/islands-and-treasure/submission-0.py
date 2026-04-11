class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[-1,0], [0,1], [1,0], [0,-1]]

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            size = len(queue)

            for i in range(size):
                row, col = queue.popleft()
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 2147483647 and (r,c) not in visited:
                        grid[r][c] = grid[row][col] + 1
                        queue.append((r,c))
                        visited.add((r,c))


        

        






        