# https://programmers.co.kr/learn/courses/30/lessons/60058
# 2020 KAKAO BLIND RECRUITMENT > 괄호 변환
from collections import deque 

def checkCorrect(obj):
    if (len(obj) == 0):
        return 1
    que = deque()
    i = 0
    while (i < len(obj)):
        if obj[i] == '(':
            que.append('(')
        elif (obj[i] == ')'):
            if (que and que[-1] == '('):
                que.pop()
            else:
                break
        i += 1
    if (i < len(obj) or que):
        return 0
    return 1
    

def divideStr(obj):
    if (len(obj) == 0):
        return "", ""
    i = 0
    cnt = 0
    while (i < len(obj)):
        if (obj[i] == '('):
            cnt += 1
        elif (obj[i] == ')'):
            cnt -= 1
        if (cnt == 0):
            break
        i += 1
    u, v = "", ""
    u = obj[:i+1]
    v = obj[i+1:]
    # print(u, v)
    return u, v
    
    

def dfs(u, v):
    if (checkCorrect(u+v)):
        return u+v
    newu, newv = divideStr(v)
    if (checkCorrect(u)):
        return u + dfs(newu, newv)
    temp = '(' + dfs(newu, newv) + ')'
    bigu = u[1:-1]
    for i in range(len(bigu)):
        if (bigu[i] == ')'):
            temp += '('
        else :
            temp += ')'
    return temp

def solution(p):
    answer = ''
    if (len(p) == 0):
        return answer
    u, v = divideStr(p)
    answer = dfs(u, v)
    print(answer)
    return answer

# solution(")(")
# solution("(()())()"	)
# solution("()))((()"	)
# # print(""[:2])