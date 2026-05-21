class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            found = set()
            for i in range(9):
                if board[r][i] == ".":
                    continue
                if board[r][i] in found:
                    return False
                found.add(board[r][i])

        for c in range(9):

            found = set()
            for i in range(9):
                if board[i][c] == ".":
                    continue
                if board[i][c] in found:
                    return False
                found.add(board[i][c])

        for square in range(9):
            found = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in found:
                        return False
                    found.add(board[row][col])
        return True