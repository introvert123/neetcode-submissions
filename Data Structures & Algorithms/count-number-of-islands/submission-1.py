class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while queue:
                row, col = queue.popleft()

                for dr,dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands
        






        