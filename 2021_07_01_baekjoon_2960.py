# https://www.acmicpc.net/problem/2960

import sys

n, k = map(int, input().split())
is_prime = [0] * (n+1)
count = 0
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if is_prime[j] == 0:
            is_prime[j] = 1
            count += 1
            if count == k:
                print(j)
                sys.exit(0)