# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십 > 튜플

from functools import cmp_to_key

def compare(item1):
    return (len(item1))

# s1 = s.lstrip('{').rstrip('}').split('},{') 이게 더 나음
def make_list(s, answer):
    i = 1
    finlst = []
    while (1):
        if (s[i] == '}' and s[i + 1] == '}'):
            # print("reached end")
            break 
        elif i != 1:
            i += 2
        tmp = []
        if s[i] == '{':
            j = i
            while s[j] != '}':
                j += 1
            tmp = s[i+1:j].split(',')
            i = j
            finlst.append(tmp)
    return finlst

def solution(s):
    answer = []
    slst = make_list(s, answer)
    slst = sorted(slst, key=compare) # key=len이 더 나음
    finaltuple = []
    for item in slst:
        for j in item:
            if int(j) not in finaltuple: # int()는 꼭 필요하다
                finaltuple.append(int(j))
    return finaltuple

# 모범풀이 
# 굳이 리스트로 다시 만들지 않고 그냥 숫자만 쭉 읽으면서 없었던 숫자 더해도 된다! 
# def solution(s):
#     answer = []

#     s1 = s.lstrip('{').rstrip('}').split('},{')

#     new_s = []
#     for i in s1:
#         new_s.append(i.split(','))

#     new_s.sort(key = len)

#     for i in new_s:
#         for j in range(len(i)):
#             if int(i[j]) not in answer:
#                 answer.append(int(i[j]))

#     return answer