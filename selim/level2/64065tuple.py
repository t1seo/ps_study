# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십 > 튜플

def solution(s): # 2021-12-17 
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)
    answer = []
    for item in s:
        intLst = item.split(',')
        for c in intLst:
            if int(c) not in answer:
                answer.append(int(c))
    return (answer)

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