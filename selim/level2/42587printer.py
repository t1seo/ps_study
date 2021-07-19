# https://programmers.co.kr/learn/courses/30/lessons/42587#
# 스택/큐 > 프린터

from collections import deque 

def solution(priorities, location):
    answer = 0
    
    que = deque()
    for idx, item in enumerate(priorities):
        que.append((item, idx))
    # print(que)
    
    while (que):
        #우선 가장 왼쪽에 있는 숫자를 뽑는다
        top = que.popleft()
        
        # 현재 스택에 있는 값이 top보다 더 크면 top을 가장 마지막에 도로 넣는다.
        if que and max(que)[0] > top[0]:
            que.append(top)
        # 만약 que가 비워져 있거나 max보다 top이 더 값이 크면 
        # 도로 넣지 않고 인쇄한다.  
        else:
            answer += 1
            # [1] 즉 idx가 우리가 원하는 location이면 탈출한다. 
            if top[1] == location:
                break
    return answer

# [1,2,3], 0 -> 3 ---> 이것때문에 어려웠다!!
# [3], 0 -> 1 
