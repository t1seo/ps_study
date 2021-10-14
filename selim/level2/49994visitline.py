# https://programmers.co.kr/learn/courses/30/lessons/49994
# Summer/Winter Coding(~2018) > 방문 길이

keys = ['U', 'D', 'R', 'L']
moves = [[0,1], [0,-1], [1,0], [-1,0]]

def solution(dirs):
    answer = 0
    x, y = 0, 0
    visited = []
    for i in range(len(dirs)):
        ind = keys.index(dirs[i]) # U라면 0이 return 
        tmpx = x + moves[ind][0] # tmp 이동하고 난 후 
        tmpy = y + moves[ind][1]
        if (tmpx < -5 or tmpx > 5 or tmpy > 5 or tmpy < -5): # out of range
            # 정작 x, y는 움직이지 않았으므로 그대로 다시 나가기 
            continue 
        if (tmpx, tmpy, x, y) not in visited: # 이동전 이동후가 없는 경우 
                                              # 이동후 이동전으로 체크해도 된다  
            visited.append((tmpx, tmpy, x, y)) # 이동후 이동전
            visited.append((x, y, tmpx, tmpy)) # 이동전 이동후 (반대) visited에 추가
            answer += 1                       # 겹치지 않았던 경우므로 ans += 1
        x = tmpx # 움직인 곳 업데이트 (if문 밖이어야 한다 )
        y = tmpy
    return answer

"""모범코드 
visited를 아예 set()로 설정해서 if in 문이 없다 
"""