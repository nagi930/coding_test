# https://www.acmicpc.net/problem/14502

from collections import deque
from copy import deepcopy


def main(cnt):
    global max_
    if cnt == 0:
        zeros = 0
        temp = deepcopy(board)
        for i in range(row):
            for j in range(col):
                if temp[i][j] == 2:
                    queue.append((i, j))
                    while queue:
                        virus = queue.popleft()
                        for k in range(4):
                            x = virus[1] + dx[k]
                            y = virus[0] + dy[k]
                            if 0 <= x <= col-1 and 0 <= y <= row-1 and temp[y][x] == 0:
                                temp[y][x] = 2
                                queue.append((y, x))
        for i in range(row):
            for j in range(col):
                if temp[i][j] == 0:
                    zeros += 1
        max_ = max(max_, zeros)

    else:
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0:
                    board[i][j] = 1
                    main(cnt-1)
                    board[i][j] = 0


if __name__ == '__main__':
    row, col = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    max_ = 0
    main(3)
    print(max_)