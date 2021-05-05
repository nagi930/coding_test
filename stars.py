from math import tan, radians
from itertools import combinations

if __name__ == '__main__':
    n = 100

    board = [['*'] * n for _ in range(n)]
    comb = list(combinations(range(1, 6), 2))
    conditions = {1: 'tan(radians(72)) * (n//2-col) > row',
                  2: 'tan(radians(72)) * (col - n//2) > row',
                  3: 'tan(radians(36)) * (n//2) > row',
                  4: 'tan(radians(36)) * (n//2 + col) < row',
                  5: 'tan(radians(36)) * (-col + (3*n)//2) < row'}
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            for c in comb:
                i, j = c
                if eval(conditions[i]) and eval(conditions[j]):
                    if board[row][col] == '*':
                        board[row][col] = ' '
                    else:
                        board[row][col] = '*'

    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=' ')
        print()
