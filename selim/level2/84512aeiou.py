# https://programmers.co.kr/learn/courses/30/lessons/84512
# 위클리 챌린지 > 5주차 > 모음사전

# 알파벳 하나마다 (5^4 +5^3 + 5^2 + 5 + 1) 로  781개 

abc = "AEIOU"

def make_bucket(): # [1, 6, 31, 156, 781]
    bucket = []
    bucket.append(1)
    for i in range(1,5):
        bucket.append(5**i + bucket[i-1])
    return bucket

def solution(word):
    answer = 0
    bucket = make_bucket()
    print(bucket)
    for i in range(len(word)):
        ind = abc.find(word[i])
        answer += bucket[4-i] * (ind) + 1
    return answer