# https://www.acmicpc.net/problem/5430

from collections import deque

n = int(input())
for _ in range(n):
    queries = list(input())
    m = int(input())
    nums = deque(eval(input()))
    reverse = False
    count = [0, 0]
    for idx, query in enumerate(queries):

        if query == 'D':
            if reverse is True:
                count[1] += 1
            else:
                count[0] += 1
        elif query == 'R':
            if reverse is True:
                reverse = False
            else:
                reverse = True

        if idx == len(queries)-1:
            try:
                for _ in range(count[0]):
                    nums.popleft()
                for _ in range(count[1]):
                    nums.pop()
            except IndexError:
                print('error')
                break
            if reverse is True:
                nums = reversed(nums)
            print(f"[{','.join(list(map(str, nums)))}]")
