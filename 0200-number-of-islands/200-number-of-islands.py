class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"

                if i > 0:
                    dfs(i-1,j)
                if j > 0:
                    dfs(i,j-1)
                if i < rows - 1:
                    dfs(i+1,j)
                if j < cols - 1:
                    dfs(i,j+1) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count