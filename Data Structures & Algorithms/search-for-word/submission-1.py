class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, depth):
            if depth == len(word):
                return True
            
            if (row<0 or row>=ROWS) or (col<0 or col>=COLS) or board[row][col] != word[depth]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                val = dfs(nr, nc, depth+1)
                if val:
                    break

            board[row][col] = temp
            return val
        

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for  c in range(COLS):
                if board[r][c] == word[0]:
                    print(r, c)
                    if dfs(r, c, 0):
                        return True

        return False
