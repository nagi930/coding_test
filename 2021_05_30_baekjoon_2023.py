# https://www.acmicpc.net/problem/2023

n = int(input())

def check(s):
    for i in range(2, s):
        if i ** 2 > s:
            break
        if s % i == 0:
            return False
    return True

def dfs(L, s):
    if L == n:
        print(s)
    else:
        for i in range(1, 10):
            if check(int(s + str(i))):
                dfs(L+1, s+str(i))

dfs(1, '2')
dfs(1, '3')
dfs(1, '5')
dfs(1, '7')