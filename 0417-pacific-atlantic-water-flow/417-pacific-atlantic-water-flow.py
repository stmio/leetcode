class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        pacific = {(i, 0) for i in range(n)} | {(0, i) for i in range(m)}
        atlantic = {(n - 1, i) for i in range(m)} | {(i, m - 1) for i in range(n)}
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(x, y, s):
            for i, j in dirs:
                if (x + i, y + j) in s or not (0 <= x + i < n and 0 <= y + j < m):
                    continue

                if heights[x + i][y + j] >= heights[x][y]:
                    s.add((x + i, y + j))
                    dfs(x + i, y + j, s)

        for x, y in list(pacific):
            dfs(x, y, pacific)
        
        for x, y in list(atlantic):
            dfs(x, y, atlantic)

        return list(atlantic & pacific)

        

