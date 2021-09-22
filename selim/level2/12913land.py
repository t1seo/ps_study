# https://programmers.co.kr/learn/courses/30/lessons/12913
# 연습문제 > 땅따먹기

def solution(land):
    answer = 0
    row = len(land)
    if (row == 1):
        return max(land[0])
    for i in range(1, row):
        for j in range(4):
            tmp = land[i-1].copy()
            tmp[j] = 0
            land[i][j] += max(tmp)
    return max(land[row-1])

"""모범코드 슬라이스로 필요없는 한 부분만 제외하기
land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
"""