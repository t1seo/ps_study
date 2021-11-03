# https://programmers.co.kr/learn/courses/30/lessons/12945
# 연습문제 > 피보나치 수 

bucket = [0] * 100001

def dFs(n):
    if (n <= 5): # 3까지가 일반적  
        return bucket[n]
    for x in range(5, n+1): # bucket의 가장 첫부터 순서대로 쌓아야 재귀가 너무 깊어지지 않음 
        bucket[x] = bucket[x-1]%1234567 + bucket[x-2]%1234567
    return bucket[n]

def solution(n):
    answer = 0
    bucket[0] = 0
    bucket[1] = 1
    bucket[2] = 1
    bucket[3] = 2
    bucket[4] = 3
    bucket[5] = 5
    answer = dFs(n) % 1234567
    # print(dFs(1000))
    return answer