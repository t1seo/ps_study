# https://programmers.co.kr/learn/courses/30/lessons/43165#qna
# 깊이/너비 우선 탐색(DFS/BFS) > 타겟넘버
def Dfs(idx, numbers, target, summ):
    global answer3
    
    N = len(numbers)
    if (idx == N):
        if (target == summ):
            answer3 += 1
        return 
    Dfs(idx + 1, numbers, target, summ+numbers[idx])
    Dfs(idx + 1, numbers, target, summ-numbers[idx])
    

def solution(numbers, target):
    global answer3
    answer3 = 0
    Dfs(0, numbers, target, 0)
    return answer3

# def solution3(numbers, target):
#     result = 0
#     def dfs(summ, level):
#         nonlocal result 
        
#         if (level == len(numbers)):
#             if (summ == target):
#                 result += 1
#             return 
        
#         dfs(summ + numbers[level], level + 1)
#         dfs(summ - numbers[level], level + 1)
        
        
#     dfs(numbers[0], 1)
#     dfs(-numbers[0], 1)
#     answer = result
#     return answer

# 모범 풀이 
# def solution2(numbers, target):
#     if not numbers and target == 0 : 
#         return 1 
#     if not numbers: 
#         return 0
#     else: 
#         return solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0])

