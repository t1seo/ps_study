# https://programmers.co.kr/learn/courses/30/lessons/12985#
# 2017 팁스타운 > 예상 대진표

import math

def solution(n,a,b):
    answer = 0
    while (True):
        if (a % 2 == 0 and b == a-1): # 1,2 3,4처럼 하나가 짝수면 홀수는 작아야 한다. 
            break
        elif (a % 2 == 1 and b == a + 1): # 하나가 홀수명 짝수는 커야 한다 
            break
        a = math.ceil(a/2) 
        b = math.ceil(b/2)
        answer += 1
    return answer + 1

""" 모범 코드 
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length() # 비트 연산인데 대단 
"""