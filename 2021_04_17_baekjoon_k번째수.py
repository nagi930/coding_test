# https://www.acmicpc.net/problem/1300

n = int(input())
k = int(input())

left = 0
right = k

while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n)
    if tmp >= k:
        num = mid
        right = mid - 1
    else:
        left = mid + 1

print(num)