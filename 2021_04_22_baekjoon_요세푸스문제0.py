# https://www.acmicpc.net/problem/11866

from collections import deque

n, m = map(int, input().split())
queue = deque(range(1, n+1))
result = []
while queue:
    for _ in range(m-1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))
print(f'<{", ".join(result)}>')