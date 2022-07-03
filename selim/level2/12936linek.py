# https://programmers.co.kr/learn/courses/30/lessons/12936?language=python3#
# 줄 서는 방법 
from math import factorial

def solution(n, k): 
    visited = [*range(1, n+1)] # range함수를 이용해서 list 만드는 방법 
    lenn = n
    answer = []
    while visited: 
        ind = (k - 1) // factorial(lenn -1)
        answer.append(visited.pop(ind))
        k -= factorial(lenn-1) * ind
        lenn -= 1
    return answer

# 힌트 얻은 곳 : https://programmers.co.kr/questions/28488

# def solution(n, k):
#     answer = [0] * n
#     visited = [0] * n
#     cnt = [0]
#     real_answer = []
#     first_number = (k-1) // factorial(n-1)
#     visited[first_number] = 1
#     answer[0] = first_number + 1
#     cnt[0] = factorial(n-1) * first_number
#     def dfs(cur_lev): 
#         if cur_lev == n : 
#             cnt[0] += 1
#             if cnt[0] >= k: 
#                 return 
#             return 
#         for i in range(len(visited)): 
#             if visited[i] == 0: 
#                 visited[i] = 1
#                 answer[cur_lev] = i+ 1
#                 dfs(cur_lev + 1)
#                 if cnt[0] >= k: 
#                     return 
#                 answer[cur_lev] = 0
#                 visited[i] = 0
#         if cnt[0] >= k: 
#             return 
#     dfs(1)
#     return answer


