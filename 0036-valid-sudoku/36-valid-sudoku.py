def column(board, col):
    return [row[col] for row in board]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First, check rows
        for row in board:
            row = [i for i in row if i != "."]
            if len(set(row)) != len(row):
                return False

        # Next check columns
        for n in range(0,9):
            col = [i for i in column(board, n) if i != "."]
            if len(set(col)) != len(col):
                return False

        # Finally, the squares
        for i in range(0,9,3):
            for j in range(0,3):
                square = list(zip(*board[i:i+3]))[3 * j : 3 * j + 3]
                square = [i for j in square for i in j if i != "."]
                if len(set(square)) != len(square):
                    return False
                
        return True