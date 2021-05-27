# https://www.acmicpc.net/problem/3055

from collections import deque
import sys

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
time = 0
water = []
queue = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            queue.append(('*', i, j, 1))

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            queue.append(('S', i, j, 1))
            while queue:
                wk, y, x, time = queue.popleft()
                if wk == '*':
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx <= c-1 and 0 <= yy <= r-1 and (board[yy][xx] == '.' or board[yy][xx] == 'S'):
                            board[yy][xx] = '*'
                            queue.append(('*', yy, xx, time+1))
                elif wk == 'S':
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx <= c-1 and 0 <= yy <= r-1 and board[yy][xx] == 'D':
                            print(time)
                            sys.exit(0)
                        elif 0 <= xx <= c-1 and 0 <= yy <= r-1 and board[yy][xx] == '.':
                            board[yy][xx] = 'S'
                            queue.append(('S', yy, xx, time+1))
print('KAKTUS')