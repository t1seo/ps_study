# https://programmers.co.kr/learn/courses/30/lessons/92343

childLst = []
maxLst = [1, 0]

def dfs(curr_ind, s_num, w_num, goLst, info):
    global childLst
    for cand in goLst:
        news_num = s_num + 1 - info[cand]
        neww_num = w_num + info[cand]
        if news_num <= neww_num:
            continue
        else : 
            newLst = goLst + childLst[cand]
            newLst.remove(cand)
            maxLst[0] = max(maxLst[0], news_num)
            maxLst[1] = max(maxLst[1], neww_num)
            dfs(cand, news_num, neww_num, newLst, info)
    

def solution(info, edges):
    global childLst
    answer = 0
    childLst = [[] for _ in range(len(info))]
    for ed in edges:
        childLst[ed[0]].append(ed[1])
    print(childLst)
        
    dfs(0, 1, 0, childLst[0], info)
    return maxLst[0]

# ex1) [0,1] [[0,1]] 1
