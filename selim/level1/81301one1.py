# https://programmers.co.kr/learn/courses/30/lessons/81301
# 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어


namelst = ['zero', 'one', 'two', 'three', 'four', 'five', \
          'six', 'seven', 'eight', 'nine']
ncntlst = [4,3,3,5,4,4,3,5,5,4]

def solution(s):
    answer = 0
    i = 0
    while (i < len(s)):
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            answer = answer * 10 + int(s[i])
            i += 1
        for j in range(10):
            if s[i : i + ncntlst[j]] == namelst[j]:
                answer = answer * 10 + j
                i += ncntlst[j] - 1
                break 
        i += 1
    return answer
"""
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""