# https://www.acmicpc.net/problem/2493

import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))[::-1]
ans = [0] * n
stack = []

for idx, top in enumerate(tops):
    while stack and stack[-1][1] < top:
        index, t = stack.pop()
        ans[n - 1 - index] = n - idx
    stack.append((idx, top))

print(' '.join(map(str, ans)))
