# 미친 로봇
# https://www.acmicpc.net/problem/1405


n, E, W, S, N = list(map(int, input().split()))
cardinal = [E/100, W/100, S/100, N/100]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(L, p, xx, yy):
    global answer
    if L == n:
        answer += p
    else:
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]
            if check[y][x] == 1:
                continue
            else:
                check[y][x] = 1
                dfs(L+1, p*cardinal[i], x, y)
                check[y][x] = 0

answer = 0
check = [[0] * 29 for _ in range(29)]
check[14][14] = 1
dfs(0, 1, 14, 14)

print(f'{answer:.15f}')

