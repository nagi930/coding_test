n, E, W, S, N = map(int, input().split())
cardinal = [E/100, W/100, S/100, N/100]

def dfs(L, p):
    global orders, answer
    if ('S' in orders and 'N' in orders) or ('W' in orders and 'E' in orders):
            return
    if L == n:
            answer += p
    else:
        for i in range(4):
            orders += c[i]
            dfs(L+1, p*cardinal[i])
            orders = orders[:-1]

answer = 0
orders = ''
c = 'EWSN'
dfs(0, 1)

print(f'{answer:.10f}')

