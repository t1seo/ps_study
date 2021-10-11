# https://programmers.co.kr/learn/courses/30/lessons/12924
# 연습문제 > 숫자의 표현 

def solution(n):
    answer = 0
    a = 1 # 곱하는 정수
    b = 0 # 더하는 정수
    i = 0
    result = []
    while (True):
        x = (n - b) / a
        if (x < 1):
            break
        if x.is_integer():
            result.append(x)
        a += 1
        i += 1
        b += i
    print(result)
    return len(result)