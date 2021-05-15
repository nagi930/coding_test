from collections import deque
import sys

col, row = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
queue = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = -1

for i in range(row):
    for j in range(col):
        if board[i][j] == 1:
            queue.append((i, j))

while queue:
    count = len(queue)
    while count > 0:
        row_, col_ = queue.popleft()
        count -= 1
        for i in range(4):
            x = col_ + dx[i]
            y = row_ + dy[i]
            if 0 <= x <= col-1 and 0 <= y <= row-1 and board[y][x] == 0:
                board[y][x] = 1
                queue.append((y, x))
    ans += 1

for i in range(row):
    for j in range(col):
        if board[i][j] == 0:
            print(-1)
            sys.exit(0)
print(ans)
