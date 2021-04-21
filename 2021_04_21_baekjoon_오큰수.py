# https://www.acmicpc.net/problem/17298

n = int(input())
nums = list(map(int, input().split()))

stack = []
ords = []
for idx, num in enumerate(nums):
    while stack and stack[-1][1] < num:
        popped = stack.pop()
        ords.append((popped[0], num))
    stack.append((idx, num))
while stack:
    popped = stack.pop()
    ords.append((popped[0], -1))

for ord in sorted(ords, key=lambda x: x[0]):
    print(ord[1], end=' ')
