# https://programmers.co.kr/learn/courses/30/lessons/42883#
# 탐욕법(Greedy) > 큰 수 만들기

from collections import deque
import sys 

def solution(number, k):
    bucket = deque()
    answer = ''
    cnt = 0
    for i, item in enumerate(number):
        while (bucket):
            if (bucket[-1] < item):
                bucket.pop()
                cnt += 1
                if (cnt == k):
                    break
            else:
                break
        bucket.append(item)
        if (cnt == k):
            break
    for x in range(0, len(bucket)): # 여길 k라고 써서 에러남 
        answer += bucket[x]
    answer += number[i + 1:]
    answer = answer[:len(answer) - (k - cnt)]
    return answer

# 백준용
# n, k = map(int, sys.stdin.readline().split())
# number = input()
# print(solution(number, k))

# 반례  
#  "999", 2 -> "9" 
# "1111", 2 -> "11"
# "9929191", 5 -> "99"