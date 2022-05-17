# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기 

def solution(s):
    answer = []
    i = 0
    for i in range(len(s)):
        src = s[i]
        # s = s[:1] 연산이 너무 많이 걸린다. 인덱스로 접근해야. 
        if answer and answer[-1] == src:
            answer.pop()
        else:
            answer.append(src)
    if (answer):
        return 0
    return 1