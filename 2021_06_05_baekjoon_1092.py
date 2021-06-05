# https://www.acmicpc.net/problem/1092

import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(boxes) > max(cranes):
    print(-1)
    sys.exit(0)

time = 0
cranes.sort(reverse=True)
boxes.sort(reverse=True)

while True:
    if not boxes:
        break
    for crane in cranes:
        if not boxes:
            break
        for j, box in enumerate(boxes):
            if crane >= box:
                del boxes[j]
                break
    time += 1

print(time)