# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3
# 찾아라 프로그래밍 마에스터 > 폰켓몬

from collections import Counter

# 처음에 짰던 코드 
def solution1(nums):
    answer = 0
    # 최근에 배운 Counter를 써서 list를 변환해서 중복 요소를 없앴다. 
    c = Counter(nums) 

    # 리스트의 절반 개수와 중복을 제거한 리스트 중 더 적은 수를 답에 넣는다 
    if (len(nums) / 2) > len(c):
        answer = len(c)
    else:
        answer = len(nums) / 2
    return answer

# better
def solution(nums):
    # 모범 코드는 set()로 중복 요소를 없앴다.  
    c = set(nums)
    answer = min(len(nums) / 2 , len(c))
    return answer
