# https://programmers.co.kr/learn/courses/30/lessons/1844
# Game map shortest distance

from collections import deque

def solution(maps):
    # me : (1,1) you: (n, m)
    # 0 wall 1 ok 
    n, m = len(maps), len(maps[0])
    sign = [(0,1), (0,-1), (1,0), (-1,0)]
    que = deque()
    que.append([0,0,1]) # y, x, lev
    answer = float('inf')
    while que:
        oldy, oldx, oldlev = que.popleft()
        if oldy == n-1 and oldx == m-1:
            answer = min(oldlev, answer)
            break 
        if oldlev > answer : 
            continue 
        for i in range(4):
            newy = oldy + sign[i][0]
            newx = oldx + sign[i][1]
            if newy >= n or newy < 0 or newx >= m  or newx < 0:
                continue 
            if maps[newy][newx] == 0:
                continue 
            maps[newy][newx] = 0 # visited -> timeout 
            que.append([newy, newx, oldlev+1])   
        # print(list(que))
    if answer == float('inf'):
        return -1
    return answer