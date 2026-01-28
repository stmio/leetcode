class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = set()
        rotten = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    rotten.add((r,c))

        ct = 0
        l = len(fresh)
        while fresh:
            rotting = set()
            for r,c in rotten:
                for dir in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                    if dir in fresh:
                        fresh.remove(dir)
                        rotting.add(dir)

            rotten.update(rotting)

            if l == len(fresh):
                return -1

            ct += 1
            l = len(fresh)

        return ct
