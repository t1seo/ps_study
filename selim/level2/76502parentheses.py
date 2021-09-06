# https://programmers.co.kr/learn/courses/30/lessons/76502
# 월간 코드 챌랜지 시즌2 > 괄호 회전하기

from collections import deque

def checkStr(s):		
    que = deque() # 스택을 이용해서 푼다 
    que.append(s[0]) # 닫는 괄호여도 일단 처음꺼는 넣는다 
    i = 1
    lenn = len(s)
    while (i < lenn):
        if s[i] == '[' or s[i] == '(' or s[i] == '{': # [({ 부분만 que에 들어가게 된다. 
            que.append(s[i])
            i += 1
        elif que:
            c = que.pop() # 짝지어서 pop 시키는데 남아있는 경우가 있으면 그건 올바르지 않은 문자열 
            if s[i] == ']' and c == '[':
                i += 1
            elif s[i] == '}' and c == '{':
                i += 1
            elif s[i] == ')' and c == '(':
                i += 1
            else:
                return 0 # 만약 짝지어지지 않으면 올바르지 않는 문자열 ex '{' ')'
        else:
            return 0 # 만약 que가 비워져 있는데 }])를 만난 경우 올바르지 않은 문자열 
    if que:
        return 0 # 만약 다 끝났는데 남아있는 경우가 있을 때 올바르지 않은 문자열 
    return 1 # 다 거치고도 오류가 없으면 answer += 1
        

def solution(s):
    answer = 0
    if len(s) == 1:
        return 0
    for i in range(len(s)):
        answer += checkStr(s)
        s = s[1:] + s[0]
    return answer