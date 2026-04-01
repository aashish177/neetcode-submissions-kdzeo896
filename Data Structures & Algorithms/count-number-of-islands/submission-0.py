class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = (row+dr), (col+dc)
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[row+dr][col+dc] = "0"

        island = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": 
                    bfs(r, c)
                    print(r, c)
                    island += 1

        return island
