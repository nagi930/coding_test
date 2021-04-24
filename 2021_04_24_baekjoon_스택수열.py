# https://www.acmicpc.net/problem/1874

from collections import deque

n = int(input())
temp, stack, answer = deque(), [], []
for _ in range(n):
    temp.append(int(input()))

for i in range(1, n+1):
    stack.append(i)
    answer.append('+')
    while stack and stack[-1] == temp[0]:
        stack.pop()
        temp.popleft()
        answer.append('-')

if stack:
    print('NO')
else:
    print('\n'.join(answer))
