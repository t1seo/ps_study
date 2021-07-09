# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
# 완전탐색 > 모의고사 

def solution(answers):
    per1 = [1,2,3,4,5]
    per2 = [2,1,2,3,2,4,2,5]
    per3 = [3,3,1,1,2,2,4,4,5,5]
    sumup = [0,0,0]
    maxlen = len(answers)
    for i in range(0, maxlen):
        if (per1[i % 5] == answers[i]):
            sumup[0] += 1
        if (per2[i % 8] == answers[i]):
            sumup[1] += 1
        if (per3[i % 10] == answers[i]):
            sumup[2] += 1
    maxnum = max(sumup)
    answer = []
    for i in range(0, len(sumup)):
        if sumup[i] == maxnum:
            answer.append(i + 1)
    return answer

"""
enumerate를 사용해도 좋음 
tuple형태 반환을 이용하여 아래처럼 활용할 수 있습니다.
>>> for i, v in enumerate(t):
...     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52
"""
