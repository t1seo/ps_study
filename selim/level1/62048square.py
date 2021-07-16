# https://programmers.co.kr/learn/courses/30/lessons/62048
# Summer/Winter coding(2019) > 멀쩡한 사각형 

import math

def solution(w,h):
    # 정사각형
    if (w == h):
        return w * h - w

    # w나 h가 크기가 1인 경우
    if (w == 1 | h == 1):
        return 0

    # 무조건 h가 더 길게 바꾼다
    if (w > h):
        w, h = h, w

    # bgin, end, summ 변수 초기화
    bgin, end, summ = -1, -2, 0

    # 상대적으로 짧은 w를 기준으로 1씩 커지면서 겹치는 부분을 더한다
    for i in range(0, w):
        bgin = math.floor(h * i / w) 
        ## **주의할 점! h / w * i 하면 시간 초과 및 오류 난다 부동소수점 때문에 생기는 문제라고 함**
        ## h / w * i (x) h * i / w (o)

        # 만약 floor 결과가 그 전에 ceil한 결과와 같다면 나눌 수 있는 정수(i)를 만난 것
        if (bgin == end):
            # 최대공약수까지 개수(summ) * w 나누기 i
            summ *= (w / i)
            break
        # 만약 못 만났다면 end를 구하고 계속 summ에 end - bgin의 차이만큼 더한다
        end = math.ceil(h * (i + 1) / w)
        summ += end - bgin

    # 정답은 전체(answer=w*h) - 하얀색(summ)부분
    return w * h - summ

# 모범풀이 
# def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
# def solution(w,h): return w*h-w-h+gcd(w,h)
