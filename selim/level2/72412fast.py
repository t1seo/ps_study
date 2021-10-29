from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    infokeys = {}
    for x in info:
        x = x.split()
        smallx = x[:4]
        smallval = int(x[4])
        for col in range(0, 5): # (range중요 0도 포함해야 "")
            for i in combinations(smallx, col):
                infokey = ''.join(i)
                if infokey in infokeys:
                    infokeys[infokey].append(smallval)
                else : 
                    infokeys[infokey] = [smallval]
    for k in infokeys:
        infokeys[k].sort()
    querydict = {}
    answer = []
    for x in query:
        x = x.split()
        querykey = x[:-1]
        queryval = int(x[-1])
        while 'and' in querykey:
            querykey.remove('and')
        while ('-') in querykey :
            querykey.remove('-')
        cnt = 0
        querykey = ''.join(querykey)
            
        if querykey in infokeys:
            scores = infokeys[querykey]
            if (scores): # 여기 조금 고쳤다고 엄청 빨라짐 
                point = bisect_left(scores, queryval)
                answer.append(len(scores) - point)
        else:
            answer.append(0)
    return answer

"""
계속 query가 길이가 긴 경우 효율성 실패했는데 
기존 이 부분을 

            if (scores):
                point = bisect_left(scores, queryval)
                point = len(scores)-point
            answer.append(point)
            
를 자기자신한테 빼는 경우를 삭제했더니 빨라졌다 
            if (scores): # 여기 조금 고쳤다고 엄청 빨라짐 
                point = bisect_left(scores, queryval)
                answer.append(len(scores) - point)
            
point = len(scores)-point 이게 생각보다 시간을 잡아먹는듯 
"""
