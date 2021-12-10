# https://programmers.co.kr/learn/courses/30/lessons/68936#
# 월간 코드 챌린지 시즌1 > 쿼드 압축 후 개수 세기 

# 모든 영역이 다 0과 1로 이루어졌는지 먼저 체크하고 재귀에 들어가야 한다 
""" 
1. 영역 모두 0, 1로 이루어졌는지 체크 
2. 1이 아니면 4영역으로 나누어 확인 
"""

codes = {'lefttop':0, 'righttop':1, 'leftbottom':2, 'rightbottom':3}
results = [0, 0]

def getstList(st, n, arr, code):
    xst = st[0]
    yst = st[1]
    if codes['lefttop'] == code:
        x0, x1 = xst, xst + n // 2 # 0, 4
        y0, y1 = yst, yst + n // 2 # 0, 4
    elif codes['righttop'] == code:
        x0, x1 = xst + n // 2, xst + n
        y0, y1 = yst, yst + n // 2
    elif codes['leftbottom'] == code:
        x0, x1 = xst, xst + n // 2
        y0, y1 = yst + n // 2, yst + n
    else:
        x0, x1 = xst + n // 2, xst + n
        y0, y1 = yst + n // 2, yst + n
        
    return ([x0, y0])

def check_nums(st, n, arr, code):
    xst = st[0]
    yst = st[1]
    if codes['lefttop'] == code:
        x0, x1 = xst, xst + n // 2 # 0, 4
        y0, y1 = yst, yst + n // 2 # 0, 4
    elif codes['righttop'] == code:
        x0, x1 = xst + n // 2, xst + n
        y0, y1 = yst, yst + n // 2
    elif codes['leftbottom'] == code:
        x0, x1 = xst, xst + n // 2
        y0, y1 = yst + n // 2, yst + n
    else:
        x0, x1 = xst + n // 2, xst + n
        y0, y1 = yst + n // 2, yst + n
    
    summ = 0
    for i in range(x0, x1):
        for j in range(y0, y1):
            summ += arr[j][i]
    return summ

def dfs(n, arr, xs):
    global results
    if n == 2:
        tmps = []
        for i in range(xs[0], xs[0]+2):
            for j in range(xs[1], xs[1]+2):
                tmps.append(arr[j][i])
        if tmps.count(0) == 4:
            results[0] += 1
        elif tmps.count(1) == 4:
            results[1] += 1
        else:
            results[0] += tmps.count(0)
            results[1] += tmps.count(1)
        return 
    for i in range(0, 4):
        ret = check_nums(xs, n, arr, i)
        if ret == 0 : 
            results[0] += 1
        elif ret == (n // 2)**2:
            results[1] += 1
        else:
            newxs = getstList(xs, n, arr, i)
            dfs(n // 2, arr, newxs)
        
        

def solution(arr):
    n = len(arr) # 가로 세로 길이 
    if n == 1:
        results[arr[0][0]] += 1
        return results
    tmpsum = 0
    for i in range(n):
        for j in range(n):
            tmpsum += arr[j][i]
    if tmpsum == 0:
        return [1, 0]
    elif tmpsum == (n **2):
        return [0, 1]
    dfs(n, arr, [0, 0])
    return results