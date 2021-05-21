# https://www.acmicpc.net/problem/5014

from collections import deque
import sys

floor, start, goal, up, down = map(int, input().split())

queue = deque()
queue.append(start)
click = 0
visited = {start}
while queue:
    cnt = len(queue)
    while cnt > 0:
        now = queue.popleft()
        cnt -= 1

        if goal < now:
            if down > 0 and 0 < now - down and now - down not in visited:
                queue.append(now - down)
                visited.add(now - down)
            if up > 0 and now + up <= floor and now + up not in visited:
                queue.append(now + up)
                visited.add(now + up)

        elif now < goal:
            if up > 0 and now + up <= floor and now + up not in visited:
                queue.append(now + up)
                visited.add(now + up)
            if down > 0 and 0 < now - down and now - down not in visited:
                queue.append(now - down)
                visited.add(now - down)
        else:
            print(click)
            sys.exit(0)
    click += 1
print('use the stairs')


