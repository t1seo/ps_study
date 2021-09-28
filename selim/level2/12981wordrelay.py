# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3
# Summer/Winter Coding(~2018) > 영어 끝말잇기

def solution(n, words):
    history = []
    history.append(words[0])
    lenn = len(words)
    a, b = 0, 0
    for i in range(1, lenn):
        if words[i-1][-1] != words[i][0] or words[i] in history:
            a = (i+1) % n 
            if (a == 0):
                a = n
            b = i//n +1
            return [a, b]
        history.append(words[i])
    return [a, b]

"""모범코드
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
"""