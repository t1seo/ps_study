# https://programmers.co.kr/learn/courses/30/lessons/42839
# 완전탐색 > 소수 찾기 lv.2

answerlst = []

def is_prime(x): # 소수가 맞다면 1을 return 
    if x <= 1: 
        return 0
    if x == 2:
        return 1
    if x % 2 == 0: 
        return 0
    for n in range(2, x):
        if (x % n == 0):
            return 0
        else :
            continue
    return 1

def dfs(num, lev, maxlev, numbers, bucket):
    if (lev == maxlev): 
        if (num not in answerlst) and is_prime(int(num)): # in보다 set()으로 중복 제거하는 것이 더 좋은 풀이인듯 
            answerlst.append(num)
        return 
    for i in range(len(numbers)):
        if bucket[i] == 0 : 		# 만약 아직 쓰이지 않은 숫자라면 
            num += str(numbers[i])	# num 뒤에 숫자를 붙인다. 
            bucket[i] = 1
            dfs(num, lev + 1, maxlev, numbers, bucket)
            bucket[i] = 0			# dfs가 끝나면 다음 반복을 위해 bucket을 다시 0으로 맞추고 
            num = num[:-1]			# num에 방금 붙인 숫자를 지운다. 
    return 
    

def solution(numbers):
    answer = 0
    bucket = [0] * len(numbers)
    for j in range(1, len(numbers) + 1):	# 1, 11, 111 과 같은 길이 
        for i in range(len(numbers)):		# 123 124 125 와 같이 numbers를 순환
            bucket[i] = 1
            if (numbers[i] != '0'):			# 맨 처음 숫자는 0이 아니어야 한다 
                dfs(str(numbers[i]), 1, j, numbers, bucket)
            bucket[i] = 0
    return len(answerlst)

# 모범풀이 보니까 set()으로 중복을 제거했더라. in 말고 set()으로 하자! 
