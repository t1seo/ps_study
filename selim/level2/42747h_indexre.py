# https://programmers.co.kr/learn/courses/30/lessons/42747#
# sort > h_index

def solution(citations):
    # 4 4 4 
    # 2 2 0 2
    newind = min(len(citations), max(citations))
    print(newind)
    citations.sort(reverse=True) # [6,5,3,1,0]
    print(citations)
    while (True):
        if citations[newind-1] >= newind : 
            break 
        else : 
            newind -= 1
    return newind