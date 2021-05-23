# https://www.acmicpc.net/problem/2589

from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(row)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

queue = deque()
max_time = 0

for i in range(row):
    for j in range(col):
        if board[i][j] == 'W':
            continue
        time = 0
        visited = [[0] * col for _ in range(row)]
        queue.append((i, j, time))
        visited[i][j] = 1

        while queue:
            pos_y, pos_x, time = queue.popleft()

            for k in range(4):
                x = pos_x + dx[k]
                y = pos_y + dy[k]

                if 0 <= x <= col-1 and 0 <= y <= row-1 and board[y][x] == 'L' and not visited[y][x]:
                    queue.append((y, x, time+1))
                    visited[y][x] = 1
        if max_time < time:
            max_time = time
print(max_time)






