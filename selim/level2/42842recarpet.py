# https://programmers.co.kr/learn/courses/30/lessons/42842
# 완전탐색 > 카펫 

def solution(brown, yellow):
    summ = brown + yellow 
    x, y = summ / 2, 2 
    maxx = summ ** 0.5
    while y <= maxx :
        if x == int(x) and y == int(y):
            if yellow == (y-2)*(x-2):
                break
        y += 1
        x = summ / y
    return [x, y]