class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            count = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or nr >= ROWS) or (nc < 0 or nc >= COLS) or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    count += 1
            return count

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        maxA = 0
        area = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxA = max(maxA, area)

        return maxA
        