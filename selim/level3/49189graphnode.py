# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
from collections import deque

def solution(n, edge):
    answer = 0
    vertex = [[] for _ in range(n+1)]
    for v in edge:
        vertex[v[0]].append([v[0],v[1]])
        vertex[v[1]].append([v[1],v[0]])
    distance = [0] * (n+1)
    distance[0], distance[1] = -1,1
    nextlst = deque(vertex[1])
    while nextlst:
        a = nextlst.popleft()
        if not distance[a[1]]:
            distance[a[1]] = distance[a[0]] + 1
            nextlst.extend(vertex[a[1]])
    maxx = max(distance)
    for item in distance:
        if maxx == item :
            answer += 1
    return answer