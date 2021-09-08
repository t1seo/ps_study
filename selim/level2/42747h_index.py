# https://programmers.co.kr/learn/courses/30/lessons/42747#
# 정렬 > H-Index

"""
citations	return
[3, 0, 6, 1, 5]	3
"""
def solution(citations):
    answer = 0
    citations.sort(reverse=True) # [6,5,3,1,0]
    lenn = len(citations)
    for i in range(lenn):
        if citations[i] < i+1: # 1, 4같은 경우 -> 그 전 인덱스를 돌려준다 
            answer = i
            break
        else:
            continue
    if answer == 0: # 만약 다 거치고 하나도 안 바뀌었다면 [42,24] 같은 케이스가 있을 수도 
        for i in range(lenn): 
            if (citations[i] < lenn): # 이 경우에는 lenn 보다 모두 큰지 확인 
                return answer
        answer = lenn # 맞다면 배열 길이를 답으로 한다 
    return answer

"""모범코드 천재인듯?!
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) 
    ### 인덱스랑 값이랑 min을 한걸 map해서 모은 후 그 map에서 가장 큰 min 값을 답에 넣는다 
    return answer
"""