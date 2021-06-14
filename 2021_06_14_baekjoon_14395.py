# https://www.acmicpc.net/problem/14395

import sys
from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    sys.exit(0)

queue = deque()
queue.append((s**2, '*'))
queue.append((s * 2, '+'))
queue.append((1, '/'))

while queue:
    num, ops = queue.popleft()
    if num == t:
        print(ops)
        sys.exit(0)
    if num < 1 or 1000000000 < num or (num == 1 and len(ops) > 1):
        continue
    queue.append((num*num, ops+'*'))
    queue.append((num+num, ops+'+'))
print(-1)






