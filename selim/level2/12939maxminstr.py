# https://programmers.co.kr/learn/courses/30/lessons/12939
# 연습문제 > 최댓값과 최솟값

def solution(s):
    answer = ''
    tmp = map(int, s.split(' '))
    numlst = sorted(list(tmp))
    answer = str(numlst[0]) + ' ' + str(numlst[-1])
    return answer
"""
모범코드
sorted 대신 max, min을 사용 
"""