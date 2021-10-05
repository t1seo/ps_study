# https://programmers.co.kr/learn/courses/30/lessons/12973#
# 2017 팁스타운 > 짝지어 제거하기

from collections import deque

def solution(s):
    que = deque()
    que.append(s[0])
    i = 1
    lenn = len(s)
    while (i < lenn): # 문자열을 한바퀴 쭉 돈다
        target = s[i] # 대상 문자가 
        if que and que[-1] == target: # que의 가장 위 문자랑 같을 때 pop
            que.pop()
        else: # 다르면 que에 추가한다
            que.append(s[i])
        i += 1
    if (que): # 한바퀴 다 돌고나서 남아있으면 cdcd 같은 형태 
        return 0
    return 1 # 비워져 있다면 baabaa 같은 형태 
    
# 더 참고할만한 케이스들 : 
# c -> 0 
# ddd -> 0

"""모범코드
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)

"""