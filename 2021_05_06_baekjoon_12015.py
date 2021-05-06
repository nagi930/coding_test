# https://www.acmicpc.net/problem/12015

n = int(input())
nums = list(map(int, input().split()))
check = []

for idx, num in enumerate(nums):
    if idx == 0:
        check.append(num)
        continue
    left, right = 0, len(check)-1
    while True:
        mid = (left + right)//2
        if check[mid] < num:
            left = mid
        else:
            right = mid

        if right-left <= 1:
            if check[left] < num <= check[right]:
                check[right] = num
            elif num > check[right]:
                check.append(num)
            else:
                check[left] = num
            break
print(len(check))