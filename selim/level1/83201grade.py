# https://programmers.co.kr/learn/courses/30/lessons/83201
# 위클리 챌린지 > 2주차 > 상호평가

from statistics import mean

def getABCD(avglst):
    ret = ''
    for i in avglst:
        if i >= 90:
            ret += 'A'
        elif i >= 80 and i < 90: 
            ret += 'B'
        elif i >= 70 and i < 80:
            ret += 'C'
        elif i >= 50 and i < 70:
            ret += 'D'
        elif i < 50:
            ret += 'F'
    return ret

def solution(scores):
    answer = ''
    avglst = [] # 평균이 들어간 리스트 
    lenn = len(scores)
    for i in range(lenn): # 학생 수 만큼 for문을 돈다 
        templst = []
        for j in range(lenn):
            templst.append(scores[j][i]) #0번 학생의 모든 점수를 다 append 
        if max(templst) == scores[i][i] and templst.count(scores[i][i]) == 1:
            templst.remove(scores[i][i])
        if min(templst) == scores[i][i] and templst.count(scores[i][i]) == 1:
            templst.remove(scores[i][i])
        # print(templst)
        avglst.append(mean(templst))
    # print(avglst)
    answer = getABCD(avglst)
    return answer

#  "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)
# ABCDF를 if elif 안 쓰고 하는 법 
