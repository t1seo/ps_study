# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
# 찾아라 프로그래밍 마에스터 > 게임 맵 최단거리 

from collections import deque 

"""
10111
10101
10111
11101
00001
"""

def is_inmap(y, x, maps):
    if (y >= len(maps) or y < 0):
        return (0)
    if (x >= len(maps[0]) or x < 0):
        return (0)
    return (1)

def solution(maps):
    bucket = [] # bucket의 용도는 개수를 세고 갔던 곳은 또 가지 않기 위해  
    for i in range(len(maps)):
        bucket.append(list())
        for j in range(len(maps[0])):
            bucket[i].append(0)
    # bucket[[0] * len(maps[0])] * len(maps)을 했더니 
    # 인덱스가 같이 수정되는 에러가... 그래서 직접 넣어주어서 만들었다 ㅜ 

    sign = [[0,-1], [0,1],[1,0],[-1,0]] #위 아래 왼오 더하기 위한 용도 
    dq = deque()
    bucket[0][0]  = 1
    dq.append([0, 0, 1]) # y, x, lev
    answer = 0
    y, x = 0, 0
    end = 0 # 변수 초기화 

    while (dq):
        oldy, oldx, oldlev = dq.popleft() # 0, 0, 1
        for i in range(4):
            y = oldy + sign[i][0]
            x = oldx + sign[i][1]
            if (is_inmap(y, x, maps) == 0): # 인덱스 에러 방지 
                continue
            if (maps[y][x] == 0): # 벽이면 continue 
                continue
            if (maps[y][x] == 1 and bucket[y][x] == 0): # 벽이 아니고, 한번도 가본적 없는 길이면 
                dq.append([y, x, oldlev + 1])           # 스택에 추가한다 
                bucket[y][x] = oldlev + 1               # 버킷에는 칸 개수를 초기화한다 
    if bucket[len(maps)-1][len(maps[0])-1] == 0:        
        return -1                                       # 버킷이 한번도 초기화되지 않으면 -1 
    return bucket[len(maps)-1][len(maps[0])-1]          # 버킷에는 답이 있으므로 return 

# 풀어보는 용 
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	

# print(solution(maps))
