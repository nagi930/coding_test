# https://www.acmicpc.net/problem/2776

def binary_search(note1, target):
    left = 0
    right = len(note1) - 1

    while left <= right:
        mid = (left + right) // 2
        if note1[mid] == target:
            return 1
        elif note1[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input())

for _ in range(n):
    m = int(input())
    note1 = list(map(int, input().split()))
    l = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for num in note2:
        print(binary_search(note1, num))
