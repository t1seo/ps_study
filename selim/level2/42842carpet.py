# https://programmers.co.kr/learn/courses/30/lessons/42842
# 완전탐색 > 카펫 

def solution(brown, yellow):

    totalsum = brown + yellow 
    for i in range(3, totalsum):
        if totalsum % i == 0: 
            garo = totalsum // i 
            if (garo - 2) * (i - 2) == yellow: 
                return [garo, i]
    return [-1, -1]

# 테스트 1을 통과못한 코드 
# import math

# FALSE = 0
# TRUE = 1

# # 소수 확인하는 코드 
# def is_prime(x):
#     if x <= 1: 
#         return FALSE
#     if x == 2:
#         return TRUE
#     if x % 2 == 0: 
#         return FALSE
#     for n in range(2, x):
#         if (x % n == 0):
#             return FALSE
#         else :
#             continue
#     return TRUE

# def solution1(brown, yellow):
#     answer = []
#     if yellow == 1 : 
#         return [3,3]
#     if yellow == 2 : 
#         return [4,3]
#     if (is_prime(yellow) == TRUE): 
#         return [yellow + 2, 3]
#     sht = 2
#     while (1):
#         if sht >= yellow / 2 : # 12 >= 12
#             return [-1, -1]
#         if (yellow % sht == 0): # 24 % 2 == 0
#             tmp = yellow // sht 
#             # print(tmp, sht)
#             if (tmp + sht + 2) * 2 == brown : 
#                 return [tmp + 2, sht + 2]
#         sht += 1 
#     return answer