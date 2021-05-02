# https://www.acmicpc.net/problem/5567

from collections import deque

m = int(input())
n = int(input())
nodes = [[] for _ in range(m+1)]
queue = deque()
for _ in range(n):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)

seen = [1]

for node in nodes[1]:
    queue.append(node)

level = 0
while queue and level < 2:
    cnt = 0
    length = len(queue)

    while cnt < length:
        cur = queue.popleft()
        cnt += 1
        if cur not in seen:
            seen.append(cur)
            for node in nodes[cur]:
                if node not in seen:
                    queue.append(node)
    level += 1

print(len(seen) - 1)
