# https://programmers.co.kr/learn/courses/30/lessons/42883#
# 탐욕법(Greedy) > 큰 수 만들기

from collections import deque
import sys 

def solution(number, k):
    bucket = deque()
    answer = ''
    cnt = 0

    # enumerate (idx, item in number) 튜플을 반환한다 
    for i, item in enumerate(number):
        
        # stack에 있는 수가 작으면 pop한다 
        while (bucket):
            if (bucket[-1] < item):
                bucket.pop()
                cnt += 1
                if (cnt == k):
                    break
            else:
                break
        # 더 큰 수를 stack에 계속 넣는다 
        bucket.append(item)
        # 만약 k개의 수를 제거했다면 for문을 탈출한다 
        if (cnt == k):
            break

    # 현재 bucket에 있는 숫자를 answer에 추가한다 
    for x in range(0, len(bucket)): # 여길 k라고 써서 에러남 
        answer += bucket[x]
    # 만약 cnt==k로 인해 일찍 break했으면 뒤에 이어서 추가한다 
    answer += number[i + 1:]
    # 만약 cnt==k가 되기 전에 for문을 다 돌았다면 cnt==k가 될때까지 뒤를 삭제한다 
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