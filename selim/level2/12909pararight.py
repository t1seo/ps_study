# https://programmers.co.kr/learn/courses/30/lessons/12909
# 연습문제 > 올바른 괄호 (정말 빠르게 해결)

from collections import deque

def solution(s):
    que = deque()
    i = 0
    while (i < len(s)):
        if s[i] == '(':
            que.append(s[i])
        elif s[i] == ')' and len(que) == 0:
            return False
        else:
            if que[-1] == ')':
                return False
            que.pop()
        i += 1
    if (que):
        return False
    return True
    
    return True