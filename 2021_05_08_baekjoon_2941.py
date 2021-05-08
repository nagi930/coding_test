# https://www.acmicpc.net/problem/2941

string = input()
finds = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
while string:
    if (1 < len(string) and string[:2] in finds):
        string = string[2:]
    elif (2 < len(string) and string[:3] in finds):
        string = string[3:]
    else:
        string = string[1:]
    cnt += 1

print(cnt)