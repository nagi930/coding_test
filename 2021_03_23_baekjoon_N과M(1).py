# N과 M (1)
# https://www.acmicpc.net/problem/15649


def dfs(L):
    if L == m:
        print(' '.join(answer))
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                answer.append(str(i))
                dfs(L+1)
                check[i] = 0
                answer.pop()

n, m = map(int, input().split())
check = [0] * (n + 1)
answer = []
dfs(0)


