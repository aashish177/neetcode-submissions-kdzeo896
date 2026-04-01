class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nr>=ROWS) or (nc<0 or nc>=COLS) or board[nr][nc] != "O":
                        continue
                    dfs(nr, nc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


