# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1
# 2021 카카오 채용연계형 인턴십 > 거리두기 확인하기

sign = [[1,0], [-1,0], [0,1], [0,-1]]

def checkdist(persn, room): # 사람을 확인하면 맨해튼 거리 확인하는 함수 
    # 만약 사람 동서남북이 모두 'x'면 통과 
    # 만약 사람 동서남북 중 'p'가 있으면 바로 fail 
    # 만약 사람 독서남북 중 'o'가 있으면 또 동서남북 확인해야한다. 
    for i in range(4):
        newy = persn[0] + sign[i][0]
        newx = persn[1] + sign[i][1]
        if (newy > 4 or newy < 0 or newx > 4 or newx < 0):
            continue 
        if (room[newy][newx] == 'X'):
            continue 
        if (room[newy][newx] == 'P'):
            return 0
        # 만약 'o'이 하나라도 있고 그 'o'주변에 사람이 있으면 fail 아닌 경우엔 continue
        for i in range(4):
            tmpy = newy + sign[i][0]
            tmpx = newx + sign[i][1]
            if tmpy == persn[0] and tmpx == persn[1]:
                continue
            if (tmpy > 4 or tmpy < 0 or tmpx > 4 or tmpx < 0):
                continue
            if room[tmpy][tmpx] == 'P':
                return 0
    return 1

def solution(places):
    answer = []
    for i in range(5): # 각 대기실 for문
        ret = 1
        for roomy in range(5): # 대기실 내 자리 for문
            for roomx in range(5):
                if places[i][roomy][roomx] == 'P':
                    ret = min(ret, checkdist([roomy, roomx], places[i]))
        answer.append(ret)
                    
    
    return answer