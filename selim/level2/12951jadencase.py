# https://programmers.co.kr/learn/courses/30/lessons/12951
# 연습문제 > JadenCase 문자열 만들기

def solution(s):
    answer = ''
    words = s.split(' ')
    for i in range(len(words)):
        word = words[i].capitalize()
        answer += word
        if (i != len(words)-1):
            answer += ' '
    return answer

""" 모범코드
return s.title()
return ' '.join([word.capitalize() for word in s.split(" ")])
"""