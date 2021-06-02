# https://www.acmicpc.net/problem/1916

import sys
import heapq

n = int(sys.stdin.readline())
b = int(sys.stdin.readline())
graph = {node : {} for node in range(1, n+1)}

for _ in range(b):
    s, e, w = map(int, sys.stdin.readline().split())
    weight = graph[s].get(e)
    if weight is None or w < weight:
        graph[s][e] = w

start, end = map(int, sys.stdin.readline().split())
distance = {node: float('INF') for node in graph}
distance[start] = 0
queue = []
heapq.heappush(queue, (distance[start], start))

while queue:
    current_distance, current_node = heapq.heappop(queue)
    if current_distance < distance[current_node]:
        continue

    for node, dis in graph[current_node].items():
        if dis + current_distance < distance[node]:
            distance[node] = dis + current_distance
            heapq.heappush(queue, (distance[node], node))

print(distance[end])