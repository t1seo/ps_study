# https://programmers.co.kr/learn/courses/30/lessons/42586
# 스택/큐 > 기능개발

from collections import deque 
# https://wikidocs.net/104977


# progresses < 100 speed <= 100
def count_days(progresses, speeds):
    dq = deque([])
    for i in range(len(progresses)):
        numm = 100 - progresses[i]
        spd = speeds[i]
        ret = 0
        if (numm % spd > 0):
            ret += 1
        ret += numm // spd
        dq.append(ret)
    return (dq)
        
    
def solution(progresses, speeds):
    dq = count_days(progresses, speeds)
    answer = list()
    past = dq[0]
    cnt = 1
    for i in range(1, len(dq)):
        if (past >= dq[i]):
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            past = dq[i]
    answer.append(cnt)
    print(dq)
    return answer
