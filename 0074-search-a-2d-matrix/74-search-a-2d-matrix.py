class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1
        ptr = None

        while l <= r:
            ptr = (l + r) // 2
            v = matrix[ptr][0]

            if v == target:
                return True
            elif target < v:
                r = ptr - 1
            else:
                l = ptr + 1

        if r < 0:
            return False

        mid = r
        l, r = 0, cols - 1

        while l <= r:
            ptr = (l + r) // 2
            v = matrix[mid][ptr]

            if v == target:
                return True
            elif target < v:
                r = ptr - 1
            else:
                l = ptr + 1

        print(mid, ptr)

        return False



