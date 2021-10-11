# https://programmers.co.kr/learn/courses/30/lessons/17677
# 2018 카카오 블라인드 채용 > [1차]뉴스 클러스터링

from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str.lower(str1)
    str2 = str.lower(str2)
    # newstr1 = ''.join(char for char in str1 if char.isalnum())
    a, b = [],[]
    for i in range(len(str1)-1):
        if str.isalpha(str1[i]) and str.isalpha(str1[i+1]):
            a.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str.isalpha(str2[i]) and str.isalpha(str2[i+1]):
            b.append(str2[i] + str2[i+1])
    # print(Counter(a))
    # print(Counter(b))
    sim = Counter(a) & Counter(b)
    summ = Counter(a) | Counter(b) # 합집합 
    cnt1, cnt2 = 0, 0
    for i in sim.keys():
        cnt1 += sim[i]
    for j in summ.keys():
        cnt2 += summ[j]
    
    if (cnt1 != 0):
        return int(cnt1 / cnt2 * 65536)
    elif (cnt1 == 0 and cnt2 == 0):
        return 1 * 65536
    else:
        return 0
    return answer

"""모범코드
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
"""