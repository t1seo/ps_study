# https://programmers.co.kr/learn/courses/30/lessons/72412
# 2021 KAKAO BLIND RECRUITMENT > 순위검색

def solution(info, query):
    answer = []
    info = [x.split() for x in info ]
    query = [x.split() for x in query]
    for x in query:
        for i in x:
            if (i == 'and'):
                x.remove(i)
    answer = []
    for wanted in query: 
        personcnt = 0
        # ['cpp', '-', 'senior', 'pizza', '250'],
        checkset = set(wanted[:4]) # string set
        checkset.discard('-')
        _cnt = 5 - len(checkset) - 1 # num of '-'
        for inf in info:
            if (len(set(inf) & checkset) == len(checkset)):
                # string 조건 일치 
                if int(inf[4]) >= int(wanted[4]):
                    personcnt += 1
        answer.append(personcnt)
    return answer