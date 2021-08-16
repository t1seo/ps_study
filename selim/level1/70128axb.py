# https://programmers.co.kr/learn/courses/30/lessons/70128
# 월간 코드 챌린지 시즌1 > 내적 

def solution(a, b):
    answer = 0
    for y, x in zip(a, b):
        answer += y*x
    return answer

# 모범코드 sum([x*y for x, y in zip(a, b)])
# lambda를 사용하는 코드 sum(map(lambda i : a[i]*b[i], range(len(a))))