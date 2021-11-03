# https://programmers.co.kr/learn/courses/30/lessons/87946#
# 위클리 챌린지 > 12주차 피로도
# 1~8이면 dfs로도 가능할듯 

visited = []
maxx = 0

def dfs(cur_hp, lv, fin_lv, dungeons):
    # print(cur_hp, lv, visited)
    global maxx
    if (lv == fin_lv+1):
        return 
    if (lv > maxx):
        maxx = lv
        # print("max", maxx, cur_hp, visited)
        
    for i in range(fin_lv):
        if (visited[i] == 0):
            if cur_hp < dungeons[i][0] : # 최소피로도 검사 
                continue
            visited[i] = 1
            dfs(cur_hp-dungeons[i][1], lv+1, fin_lv, dungeons)
            visited[i] = 0
    return 
        

def solution(k, dungeons):
    for i in range(len(dungeons)):
        visited.append(0)
    dfs(k, 0, len(dungeons), dungeons)
    return maxx