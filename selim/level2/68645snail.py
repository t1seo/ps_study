# https://programmers.co.kr/learn/courses/30/lessons/68645
# 월간 코드 챌린지 시즌1 > 삼각 달팽이 

def solution(n):
    # result = []
    # for i in range(0, n):
    #     result.append([])
    #     for j in range(0, i+1):
    #         result[i].append(0)
    result = [[0 for j in range(0, i+1)] for i in range(0, n)]
    
    y, x = -1, 0
    num = 1
    for i in range(0, n): # 첫번째 돌때는 1~6 / 두번째는 7~11.. 이렇게 채워짐
        for j in range(i, n): # 돌때마다 하나씩 줄어든다 
            # 결국 n * n+1 / 2 개수만큼 돌게 됨 
            if i % 3 == 0:
                y += 1 # 왼쪽일때는 y값이 커짐 
            elif i % 3 == 1:
                x += 1 # 바닥일때는 x 값이 커짐 
            else : 
                x -= 1
                y -= 1
                # 오른족일때는 x, y값 둘다 작아짐 
            result[y][x] = num
            num += 1
    # print(result)
    return sum(result, [])
    
    
    