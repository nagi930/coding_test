# https://www.acmicpc.net/problem/1753

import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = {node: {} for node in range(1, v+1)}
queue = []
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    weight = graph[u].get(v)
    if weight is None or w < weight:
        graph[u][v] = w
        continue

distance = {node: float('INF') for node in graph}
distance[start] = 0
heapq.heappush(queue, (distance[start], start))

while queue:
    current_distance, current_node = heapq.heappop(queue)

    if distance[current_node] < current_distance:
        continue

    for node, edge in graph[current_node].items():
        if current_distance + edge < distance[node]:
            distance[node] = current_distance + edge
            heapq.heappush(queue, (distance[node], node))

for value in distance.values():
    if value == float('INF'):
        print('INF')
    else:
        print(value)

