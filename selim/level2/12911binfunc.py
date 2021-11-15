# https://programmers.co.kr/learn/courses/30/lessons/12911
# 연습문제 > 다음 큰 숫자 
# 시간이 걸릴 것 같더라도 간혹 차례대로 보는 것도 정답이다. 

# 이진수 함수 bin()
"""
혹시 구현해야 하면 
def binn(n):
    if n == 0: return ''
    elif n % 2 == 0: return binn(n//2) + '0'
    else: return binn(n//2) + '1'
"""

def solution(n):
    answer = 0
    # print(bin(n)) # 0b1001110
    n_one = bin(n).count('1')
    print(n_one)
    for i in range(n+1, 1000001):
        if bin(i).count('1') == n_one:
            return i
    return answer