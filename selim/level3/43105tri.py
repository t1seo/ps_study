# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
# 동적계획법 > 정수 삼각형 ... 이지만 그리디에 가깝다

def solution(triangle):
    answer = 0
    height = len(triangle)
    for i in range(1, height):
        for j in range(len(triangle[i])):
            a, b = 0, 0
            if (j-1 >= 0):
                a = triangle[i-1][j-1]
            if (j < len(triangle[i-1])):
                b = triangle[i-1][j]
            triangle[i][j] += max(a, b)
    answer = max(triangle[height-1])
    return answer