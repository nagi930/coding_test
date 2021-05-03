# https://www.acmicpc.net/problem/1654

m, n = map(int, input().split())

lines = []
for _ in range(m):
    lines.append(int(input()))


left = 0
right = max(lines)

while left <= right:
    mid = (left + right) // 2 or 1

    line_num = 0
    for line in lines:
        line_num += line//mid

    if line_num < n:
        right = mid - 1
    elif line_num >= n:
        answer = mid
        left = mid + 1
print(answer)
