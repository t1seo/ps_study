# https://programmers.co.kr/learn/courses/30/lessons/42885
# 탐욕법 > 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # 오름차순으로 정렬
    que = deque(people) # popleft를 사용하기 위해 deque 소환
    while (que):
        fst = que.popleft() # 가장 큰 수를 빼낸다 
        while (que and fst + que[-1] <= limit): # 만약 가장 큰 수 와 가장 작은 수를 더했을 때 합이 limit을 넘지 않으면 계속 뺀다 
            fst += que.pop()
        answer += 1 # 만들어지는 짝만큼 answer의 개수를 더한다 
    return answer

"""모범 코드 : 투 포인터 사용해서 따로 deque를 사용하지 않음 
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
"""