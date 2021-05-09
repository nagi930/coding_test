# https://www.acmicpc.net/problem/2696

import heapq

n = int(input())
for _ in range(n):
    max_heap, min_heap = [], []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    m = int(input())
    nums = []
    for i in range(m//10+1):
        temp = list(map(int, input().split()))
        nums.extend(temp)
    for idx, num in enumerate(nums):
        if len(max_heap) <= len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if max_heap and min_heap:
            max_ = -heapq.heappop(max_heap)
            min_ = heapq.heappop(min_heap)

            if max_ > min_:
                heapq.heappush(min_heap, max_)
                heapq.heappush(max_heap, -min_)
            else:
                heapq.heappush(min_heap, min_)
                heapq.heappush(max_heap, -max_)
        if idx % 2 == 0:
            print(-max_heap[0], end=' ')
    print()





