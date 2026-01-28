class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 1:
                grid[i][j] = 0
                area = 1                  

                if i > 0:
                    area += dfs(i-1,j)
                if j > 0:
                    area += dfs(i,j-1)
                if i < rows - 1:
                    area += dfs(i+1,j)
                if j < cols - 1:
                    area += dfs(i,j+1) 

                return area

            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, dfs(r,c))

        return best