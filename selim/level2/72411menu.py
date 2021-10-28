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