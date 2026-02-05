class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        regions = { (i, j) for i in range(m) for j in range(n) if board[i][j] == "O" }
        keep = {
            (i, j) for i, j in regions
            if i == 0 or j == 0 or i == m - 1 or j == n - 1
        }

        if not keep:
            for i, j in regions:
                board[i][j] = "X"

        def dfs(x, y):
            for i, j in dirs:
                if (x + i, y + j) in keep:
                    continue
                if not (0 <= x + i < m and 0 <= y + j < n):
                    continue

                if board[x + i][y + j] == "O":
                    keep.add((x + i, y + j))
                    dfs(x + i, y + j)

        for x, y in list(keep):
            dfs(x, y)
        for x, y in (regions - keep):
            board[x][y] = "X"