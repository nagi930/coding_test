# https://www.acmicpc.net/problem/10026

from collections import deque
from copy import deepcopy

n = int(input())
board = [list(input()) for _ in range(n)]
queue = deque()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(board, check):
    new_board = deepcopy(board)
    cnt = 0
    for i in range(n):
        for j in range(n):
            rgb = new_board[i][j]
            for item in check:
                if rgb in item:
                    new_board[i][j] = '-'
                    queue.append((i, j, rgb))
                    class_ = item
                    break
            if not queue:
                continue
            while queue:
                row, col, rgb = queue.popleft()
                for k in range(4):
                    x = col + dx[k]
                    y = row + dy[k]
                    if 0 <= x <= n-1 and 0 <= y <= n-1 and new_board[y][x] in class_:
                        queue.append((y, x, rgb))
                        new_board[y][x] = '-'
            cnt += 1
    return cnt

print(bfs(board, ['R', 'G', 'B']), bfs(board, ['RG', 'B']))