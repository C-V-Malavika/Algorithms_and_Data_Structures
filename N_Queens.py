class NQueen:

    def isSafe(self, row, col, board, n):

        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True


    def solve(self, col, board, ans, n):

        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]


    def solveNQueens(self, n):

        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    n = 4
    obj = NQueen()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i+1}")
        for j in range(len(ans[0])):
            print(ans[i][j])
        print()

    print("CASE - 2")
    print("--------")
    print()

    n = 6
    obj = NQueen()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i+1}")
        for j in range(len(ans[0])):
            print(ans[i][j])
        print()