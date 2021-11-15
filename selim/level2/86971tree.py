# https://programmers.co.kr/learn/courses/30/lessons/86971
# 위클리 챌린지 > 전력망을 둘로 나누기 

from collections import defaultdict

def dfs(start, visited):
    global count
    global trees
    for i in trees[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, visited)
            count += 1
            

def solution(n, wires):
    global trees, count
    answer = -1
    trees = defaultdict(list)
    for a, b in wires: 
        trees[a].append(b)
        trees[b].append(a)
    # print(trees) defaultdict(<class 'list'>, {1: [3], 3: [1, 2, 4], 2: [3], 4: [3, 5, 6, 7], 5: [4], 6: [4], 7: [4, 8, 9], 8: [7], 9: [7]})
    cand = []
    for a, b in wires:
        trees[a].remove(b)
        trees[b].remove(a)
        count = 0
        dfs(1, [])
        cand.append(abs(n-count-count))
        trees[a].append(b)
        trees[b].append(a)
        
    return min(cand)