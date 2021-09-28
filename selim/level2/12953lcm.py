# https://programmers.co.kr/learn/courses/30/lessons/12953
# 연습문제 > N개의 최소공배수

from math import gcd

# 두 수의 최소공배수(lcm)은 두 수의 곱에서 최대공약수(gcd)를 나누면 된다. 
def getlcm(x, y):
    return x * y // gcd(x, y)

def solution(arr):
    answer = 0
    while True:
        arr.append(getlcm(arr.pop(), arr.pop())) # arr의 두 수를 계속 뽑아서 최소공배수를 만들어 추가한다.
        if (len(arr) == 1): # 하나밖에 안 남으면 그 수가 n개 수의 최소공배수가 된다
            return arr[0]
    return answer