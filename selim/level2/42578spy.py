# https://programmers.co.kr/learn/courses/30/lessons/42578
# 해시 > 위장

def solution(clothes):
    answer = 1
    closetdict = {}
    for i in range(len(clothes)):
        tmpkey = clothes[i][1]
        if tmpkey in closetdict:
            closetdict[tmpkey] += 1
        else:
            closetdict[tmpkey] = 1
    # print(closetdict)
    for val in closetdict.values(): # 수학 공식 사용. (a+1)*(b+1)* ... -1
        answer *= (val + 1)
    return answer - 1

# 모범코드 
"""
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
"""