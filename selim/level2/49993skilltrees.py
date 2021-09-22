# https://programmers.co.kr/learn/courses/30/lessons/49993
# Summer/Winter Coding > 스킬트리

def check_word(avalist, word, skill):
    for j in range(len(word)):
        if word[j] in skill:
            ind = skill.find(word[j])
            if (ind != 0 and avalist[ind-1] == 0):
                return 0
            avalist[ind] = 1
    return 1

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        avalist = [0] * len(skill)
        answer += check_word(avalist, skill_trees[i], skill)
    return answer

""" 함수 return문 말고 탈출 적용하는 방법은 for else문 
for s in skills:
    if s in skill:
        if s != skill_list.pop(0):
            break
else:
    answer += 1
"""