# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3
# 찾아라 프로그래밍 마에스터 > 폰켓몬

from collections import Counter

def solution1(nums):
    answer = 0
    c = Counter(nums)
    if (len(nums) / 2) > len(c):
        answer = len(c)
    else:
        answer = len(nums) / 2
    return answer

# better
def solution(nums):
    c = set(nums)
    answer = min(len(nums) / 2 , len(c))
    return answer
