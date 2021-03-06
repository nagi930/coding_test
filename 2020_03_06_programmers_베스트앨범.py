'''
https://programmers.co.kr/learn/courses/30/lessons/42579
베스트앨범
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
'''

from collections import defaultdict

def solution(genres, plays):
    best_album = []
    playlist = defaultdict(list)
    sum_plays = defaultdict(int)

    for (index, genre), play in zip(enumerate(genres), plays):
        playlist[genre].append([index, play])
        sum_plays[genre] += play

    for key in playlist.keys():
        playlist[key].sort(key=lambda x: (x[1], -x[0]), reverse=True)

    sorted_list = sorted(sum_plays.keys(), key=lambda x: sum_plays[x], reverse=True)

    for key in sorted_list:
        if len(playlist[key]) > 1:
            best_album.append(playlist[key].pop(0)[0])
            best_album.append(playlist[key].pop(0)[0])
        else:
            best_album.append(playlist[key].pop(0)[0])

    return best_album



# while문 사용 -> Fail, 많이 재생된 장르 ~ 장르 삭제 부분에 문제가 있는 것으로 보임
'''
from collections import defaultdict

def solution(genres, plays):
    best_album = []
    playlist = defaultdict(list)
    sum_plays = defaultdict(int)

    for (index, genre), play in zip(enumerate(genres), plays):
        playlist[genre].append([index, play])
        sum_plays[genre] += play

    for key in playlist.keys():
        playlist[key].sort(key=lambda x: (x[1], -x[0]), reverse=True)

    while sum_plays and len(best_album) < 4:
        select_genre = max(sum_plays, key=sum_plays.get)
        count = 2

        while playlist[select_genre] and count > 0 and len(best_album) < 4:
            best_album.append(playlist[select_genre].pop(0)[0])
            count -= 1
        del sum_plays[select_genre]

    return best_album
'''





print(solution(['A', 'B', 'A', 'A', 'B'], [
      500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B'], [500]) == [0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
print(solution(['c','a','b','a','a','b','b','b','b','c','c','c','d'], [1,500,9, 600, 501, 800,500,300,2,2,1,2,100000]))
print(solution(['c', 'p', 'c', 'c', 'p', 'p'], [500, 600, 150, 800, 2500, 3000]))
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 800, 800, 2500]) == [4, 1, 2, 3])