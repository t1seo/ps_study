# https://programmers.co.kr/learn/courses/30/lessons/76501
# 월간 코드 챌린지 시즌2 > 음양 더하기 

def solution(absolutes, signs):
    answer = 0
    plm = 1
    for i in range(len(signs)):
        plm = 1
        if (signs[i] == 0):
            plm = -1
        answer += absolutes[i] * plm
    return answer
