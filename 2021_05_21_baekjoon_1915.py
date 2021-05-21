# https://www.acmicpc.net/problem/1915

row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]
dp = [[0] * col for _ in range(row)]
max_ = 0

for i in range(row):
    for j in range(col):
        if board[i][j] == '0':
            continue
        else:
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif dp[i-1][j] > 0 and dp[i][j-1] > 0 and dp[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 1

        if max_ < dp[i][j]:
            max_ = dp[i][j]

print(max_**2)


