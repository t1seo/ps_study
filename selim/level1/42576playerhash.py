# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 해시 > 완주하지 못한 선수 

def solution(p, c):
    p.sort()
    c.sort()

    # 달라지는 순간은 p와 c가 다른 값이라는 뜻이다. 
    for i in range(len(p) - 1):
        if (p[i] != c[i]):
            return (p[i])
    return (p[-1])

# 모범 풀이 
# import collections
# 
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
