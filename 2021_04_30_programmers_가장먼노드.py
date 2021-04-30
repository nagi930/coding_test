from collections import deque

def solution(n, edges):
    li = [set() for _ in range(n)]
    for t, f in edges:
        li[t-1].add(f-1)
        li[f-1].add(t-1)

    queue = deque()
    queue.append(0)
    seen = [0] * n
    seen[0] = 1
    ans = []

    while queue:
        length = len(queue)
        cnt = 0
        temp = queue.copy()
        while cnt < length:
            edge = queue.popleft()
            cnt += 1
            for i, j in enumerate(li[edge]):
                if seen[j] == 0:
                    queue.append(j)
                    seen[j] = 1
        ans.append(temp)

    return len(ans[-1])

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))