# https://www.acmicpc.net/problem/1697
# 숨바꼭질

from collections import deque

n, k = map(int, input().split())
def solution(n, k):
    if n == k:
        return 0
    else : 
        visited = [0] * 100001
        que = deque()
        que.append([n, 0])
        while que:
            now, lev = que.popleft()
            for newx in [now+1, now-1, now*2]:
                if newx == k:
                    return lev+1
                if newx >= 0 and newx <= 100000 and visited[newx] == 0:
                    visited[newx] = 1
                    que.append([newx, lev+1])
print(solution(n, k))