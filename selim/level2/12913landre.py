# https://programmers.co.kr/learn/courses/30/lessons/12913
# 연습문제 > 땅따먹기

def solution(land):
    lenn = len(land) # 3
    for i in range(1, lenn):
        for j in range(0, 4):
            maxx = max(land[i-1][:j] + land[i-1][j+1:])
            land[i][j] += maxx
    return max(land[-1])
    