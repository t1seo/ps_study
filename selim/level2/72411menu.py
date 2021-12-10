# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
# 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

from itertools import combinations 
from collections import Counter

# https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC-by-Python

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            for li in combinations(order, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_cand = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_cand if cnt >1 and cnt == sorted_cand[0][1]]
    return (sorted(answer))


def solution1(orders, course): # 2021-12-10
    result = []
    combLst = []
    course.sort()
    
    for i in course:
        combLst = []
        for order in orders:
            a = list(order)
            a.sort()
            order = ''.join(a)
            if len(order) >= i:
                combLst.extend(combinations(order, i))
        c = Counter(combLst).most_common()
        # print(c)
        for j, value in c:
            if value == c[0][1] and value >= 2:
                result.append(j)
    result = [''.join(x) for x in result ]
    result.sort()
    return result