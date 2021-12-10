#https://programmers.co.kr/learn/courses/30/lessons/77484 
# 2021 Dev-Matching > 로또의 최고 순위와 최저 순위 
# 6개 일치하면 1등 
# 5 - 2
# 4 - 3 
# 3 - 4
# 2 - 5 
# 1 - 6 
# 0개 일치하면 6등 

def solution(lottos, win_nums):
    winList = [6, 6, 5, 4, 3, 2, 1] # samee == 
    zeros = 0
    samee = 0
    for num in lottos:
        if num == 0:
            zeros += 1
        else:
            if num in win_nums:
                samee += 1
    print(zeros, samee)
    lowest = winList[samee]
    highest = winList[samee + zeros]
    return [highest, lowest]
    
# def findRank(num):
#     if num <= 6 and num >= 2: 
#         return 7 - num
#     else : 
#         return 6


# def solution1(lottos, win_nums):
#     cnt, prob = 0, 0
#     for lottonum in lottos:
#         if lottonum in win_nums : 
#             cnt += 1
#         elif lottonum == 0: 
#             prob += 1
#     print(cnt, prob)
#     minn = findRank(cnt)
#     maxx = findRank(cnt + prob)
#     return [maxx, minn]