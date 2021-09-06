# https://programmers.co.kr/learn/courses/30/lessons/77484
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저순위

# 6개 일치하면 1등 
# 5 - 2
# 4 - 3 
# 3 - 4
# 2 - 5 
# 1 - 6 
# 0개 일치하면 6등  -> findRank
def findRank(num): 
    if num <= 6 and num >= 2: 
        return 7 - num
    else : 
        return 6

def solution(lottos, win_nums):
    cnt, prob = 0, 0
    for lottonum in lottos:
        if lottonum in win_nums : # win_nums에 숫자가 있는만큼 cnt += 1
            cnt += 1
        elif lottonum == 0: # 미지 숫자 '0'만큼 prob(ability) += 1
            prob += 1
    # print(cnt, prob) # check용
    minn = findRank(cnt) # 최저 순위 ex) 5등 
    maxx = findRank(cnt + prob) # 최고 순위 ex) 3등 
    return [maxx, minn] # 답은 최고-최저 순으로 ex) [3, 5]