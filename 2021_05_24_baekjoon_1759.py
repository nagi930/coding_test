# https://www.acmicpc.net/problem/1759

def dfs(L, s):
    if len(s) == l:
        count = 0
        for i in s:
            if i in 'aeiou':
                count += 1
        if count > 0 and l - count > 1:
            print(s)
            return
    if L == c:
        return
    else:
        dfs(L+1, s+chars[L])
        dfs(L+1, s)

if __name__ == '__main__':
    l, c = map(int, input().split())
    chars = sorted(list(input().split()))
    dfs(0, '')
