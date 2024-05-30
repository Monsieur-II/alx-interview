#!/usr/bin/python3
"""Solves nqeens problem"""


class Chess:
    @staticmethod
    def nQueens(n):
        # n is the size of nxn chess board
        columns = set()
        posConsts = set()
        negConsts = set()
        board = [[] for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = board.copy()
                print(copy)
                return

            for c in range(n):
                if c in columns or r + c in posConsts or r - c in negConsts:
                    continue

                columns.add(c)
                posConsts.add(r + c)
                negConsts.add(r - c)
                board[r].append(r)
                board[r].append(c)

                backtrack(r + 1)

                columns.remove(c)
                posConsts.remove(r + c)
                negConsts.remove(r - c)
                board[r].clear()

        backtrack(0)


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    Chess.nQueens(N)
