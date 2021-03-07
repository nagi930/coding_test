import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    # if all(food > K for food in scoville):
    #     return count

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        heapq.heappush(scoville, first + heapq.heappop(scoville) * 2)
        count += 1
        if all(food > K for food in scoville):
            return count

    return -1