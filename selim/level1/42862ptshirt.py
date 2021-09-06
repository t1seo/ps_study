# https://programmers.co.kr/learn/courses/30/lessons/42862
# 탐욕법(Greedy) > 체육복

def solution(n, lost, reserve):
    answer = 0
    bucket = [0] # 학생 수 와 인덱스를 맞추기 위해 미리 0번째 자리는 0이 차지
    for i in range(1, n+1):
        if i in lost and i not in reserve:
            bucket.append(0)
        elif i in lost and i in reserve: # 도난 당했는데 여분이 있을 때 체육복을 뺴온다 
            bucket.append(1)
            reserve.remove(i)
        else:
            bucket.append(1)
    cnt = 0
    for i in range(1, n+1):
        if bucket[i] == 0: # 도난 당했을 때 빌릴 수 있는지 확인하는 for문 
            if i + 1 in reserve:
                cnt += 1
                reserve.remove(i + 1)
            elif i - 1 in reserve:
                cnt += 1
                reserve.remove(i - 1)
        else:
            cnt += 1
    return cnt