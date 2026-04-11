class Solution:
    def solve(self, board: List[List[str]]) -> None:


        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):

            for dr,dc in directions:
                row = r + dr
                col = c + dc

                if row in range(rows) and col in range(cols) and board[row][col] == "O":
                    board[row][col] = "T"
                    dfs(row,col)


        #we are using the strategy of getting everything except unsurrounded = surrounded

        # what are unsurrounded?  - those which are connected to border
        #taking the ones in the border and making them O -> T

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0,rows-1] or col in [0,cols-1]):
                    board[row][col] = "T"
                    dfs(row,col)

        
        #now whatever is remaining after dfs is just the possible areas which are surrounded
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        #we change whatever has been marked by T with O again
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
                