class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c]==0):
                return 0
            
            val = 0
            print(r,c)
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                val += dfs(nr, nc)
            
            return 1 + val

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        maxA = 0
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)

                maxA = max(area, maxA)
        
        return maxA