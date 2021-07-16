# https://programmers.co.kr/learn/courses/30/lessons/12977
# Summer/Winter Coding(~2018) > 소수 만들기 
import math

FALSE = 0
TRUE = 1

# 소수 확인하는 코드 
def is_prime(x):
    if x <= 1: 
        return FALSE
    if x == 2:
        return TRUE
    if x % 2 == 0: 
        return FALSE
    for n in range(2, x):
        if (x % n == 0):
            return FALSE
        else :
            continue
    return TRUE

# while문을 여러번 돌지 않도록 미리 가장 큰 수보다 작은 소수를 미리 저장한다 
# bigsum에는 가장 큰 수 세 개를 더한 값이다. bigsum 크기만큼 bucket을 0으로 채운다. 
# 그리고 bigsum보다 작은 소수를 1로 칠한다. 
# 예시 : [0,0,1,1,0,1,0,1,...] (2, 3, 5, 7은 1이 된다 )
def dec_bucket(bigsum):
    bucket = list()
    for i in range(0, bigsum + 1):
        bucket.append(0)
    for x in range(2, bigsum + 1):
        if is_prime(x):
            bucket[x] = 1
    return (bucket)

def solution(nums):
    # 크기 순서대로 정렬 
    nums.sort() 

    # bucket 리스트에 미리 소수를 저장해둔다. 소수는 1 값을 갖는다 
    bucket = dec_bucket(nums[-1] + nums[-2] + nums[-3])
    answer = 0
    cnt = len(nums)
    for i in range(0, cnt - 2):
        for j in range(i + 1, cnt - 1):
            for k in range(j + 1, cnt):
                summ = nums[i] + nums[j] + nums[k]
                
                # bucket[idx] == 1 즉 해당 인덱스가 1이면 소수라는 뜻이다. 
                if (bucket[summ] == 1):
                    # print(summ)
                    answer += 1
    return answer
