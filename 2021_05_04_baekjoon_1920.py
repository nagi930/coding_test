# https://www.acmicpc.net/problem/1920

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

nums.sort()

for s in search:
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == s:
            print(1)
            break
        elif nums[mid] < s:
            left = mid + 1
        elif nums[mid] > s:
            right = mid - 1
    else:
        print(0)