# https://programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    sdts = {'S': 1, 'D': 2, 'T': 3}
    options = {'*': 2, '#': -1, '': 1}
    ans = 0

    darts = re.findall('([0-9]+)([SDT])([*#]*)', dartResult)
    before_score = 0
    for mark, sdt, option in darts:
        option = options[option]
        score = (int(mark) ** sdts[sdt]) * option
        if option == 2:
            ans += score + before_score
        else:
            ans += score
        before_score = score
    return ans


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
