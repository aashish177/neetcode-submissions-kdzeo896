class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        INF = 2**31 - 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (nr<0 or nr>=ROWS) or (nc<0 or nc>=COLS) or grid[nr][nc] != INF:
                    continue
                print(nr, nc)
                print(grid[r][c])
                grid[nr][nc] = grid[row][col] + 1
                print(grid)
                q.append((nr, nc))