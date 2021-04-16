# https://www.acmicpc.net/problem/9663

n = int(input())

queens = []
count = 0

def is_valid(row, col):
    if row == 0:
        return True
    if col in queens:
        return False
    else:
        for i in range(0, len(queens)):
            if abs(queens[i] - col) == row - i:
                return False
    return True

def dfs(row):
    global count
    if row == n:
        if len(queens) == n:
            count += 1
    else:
        for col in range(n):
            if is_valid(row, col):
                queens.append(col)
                dfs(row+1)
                queens.pop()

dfs(0)
print(count)