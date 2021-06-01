# https://www.acmicpc.net/problem/11559

from collections import deque

def bfs(board):
    loop = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in ['R', 'G', 'B', 'P', 'Y']:
                queue.append((i, j, board[i][j]))
                visited = {(i, j)}
                cnt = 1
                while queue:
                    row, col, color = queue.popleft()
                    for k in range(4):
                        row_ = row + dy[k]
                        col_ = col + dx[k]
                        if 0 <= row_ <= 11 and 0 <= col_ <= 5 \
                                and board[row_][col_] == color and (row_, col_) not in visited:
                            queue.append((row_, col_, color))
                            visited.add((row_, col_))
                            cnt += 1

                if cnt >= 4:
                    loop = True
                    for r, c in visited:
                        board[r][c] = '.'
    fall_blocks(board)

    return loop

def fall_blocks(board):
    for i in range(len(board[0])):
        for j in range(len(board)-1, -1, -1):
            if board[j][i] != '.':
                for k in range(len(board)-1, j, -1):
                    if board[k][i] == '.':
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break

if __name__ == '__main__':
    board = [list(input()) for _ in range(12)]
    queue = deque()

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    ans = 0

    while True:
        loop = bfs(board)
        if loop:
            ans += 1
        else:
            break
    print(ans)

