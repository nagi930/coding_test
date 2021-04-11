import heapq
import sys

max_heap = []
min_heap = []

n = int(sys.stdin.readline())

for idx, _ in enumerate(range(n)):
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -int(sys.stdin.readline()))
    else:
        heapq.heappush(min_heap, int(sys.stdin.readline()))

    if max_heap and min_heap:
        min_ = min_heap[0]
        max_ = -max_heap[0]
        if min_ < max_:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])
