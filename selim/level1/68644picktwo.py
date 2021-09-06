# https://programmers.co.kr/learn/courses/30/lessons/68644
# 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기 

def solution(numbers):
    answer = []
    sumlst = []
    for i in range(201):
        sumlst.append(0)
    for i in range(len(numbers) - 1):
        temp = numbers[i]
        for j in range(i + 1, len(numbers)):
            temp += numbers[j]
            sumlst[temp] = 1
            temp -= numbers[j]
    for i in range(201):
        if sumlst[i] == 1:
            answer.append(i)
    return answer

# 모범코드 sumlst 없이 sorted로도 충분하다. 
# 난 time consuming할까봐 bucket했는데 sorted로도 충분 
#  return sorted(list(set(answer)))