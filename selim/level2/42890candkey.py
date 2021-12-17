# https://programmers.co.kr/learn/courses/30/lessons/42890
# 2019 KAKAO BLIND RECRUITMENT > 후보키

from itertools import combinations 

def solution(relations):
    row = len(relations)
    col = len(relations[0])
    
    candidates = []
    for i in range(1, col+1): # 1~col 
        candidates.extend(combinations(range(col), i))
    """	[(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]"""
    
    uniqueness = []
    for candi in candidates: # (0, ) (1, 2)
        aflist = []
        for student in relations:
            temp = []
            for i in candi:
                temp.append(student[i])
            aflist.append(tuple(temp))
        if len(set(aflist)) == row:
            uniqueness.append(candi)
    print(uniqueness)
    
    minimal = set(uniqueness)
    for i in range(len(uniqueness)):
        for j in range(i+1, len(uniqueness)):
            aset = set(uniqueness[i])
            bset = set(uniqueness[j])
            if(len(aset & bset) == len(uniqueness[i])):
                minimal.discard(uniqueness[j])
    return (len(minimal))


def solution1(relation):
    # 1.키
    keyLst = []
    colLst = []
    for i in range(len(relation[0])):
        keyLst.append(i)
    for j in range(1, len(relation[0])+1):
        for i in combinations(keyLst, j):
            colLst.append(i)
    print(colLst)
    candLst = []
    for cols in colLst:
        tmpset = set()
        for rel in relation:
            tmp = ""
            for c in cols:
                tmp += rel[c]
            tmpset.add(tmp)
        # print(tmpset)
        if len(relation) == len(tmpset):
            candLst.append(cols)
    # print(candLst)
    oxLst = [1 for _ in range(len(candLst))]
    # print(oxLst)
    for i in range(0, len(candLst)):
        if oxLst[i] == 0:
            continue 
        for j in range(i+1, len(candLst)):
            if oxLst[j] == 1 and set(candLst[i]).intersection(set(candLst[j])) == set(candLst[i]):
                oxLst[j] = 0
            elif oxLst[j] == 1 and set(candLst[i]).intersection(set(candLst[j])) == set(candLst[j]):
                oxLst[j] = 0
    print(oxLst)
    return sum(oxLst)
    