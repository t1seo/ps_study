# https://programmers.co.kr/learn/courses/30/lessons/12977
# Summer/Winter Coding(~2018) > 소수 만들기 
import math

FALSE = 0
TRUE = 1

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

def dec_bucket(bigsum):
    bucket = list()
    for i in range(0, bigsum + 1):
        bucket.append(0)
    for x in range(2, bigsum + 1):
        if is_prime(x):
            bucket[x] = 1
    return (bucket)

def solution(nums):
    nums.sort() 
    bucket = dec_bucket(nums[-1] + nums[-2] + nums[-3])
    # print(bucket)
    answer = 0
    cnt = len(nums)
    for i in range(0, cnt - 2):
        for j in range(i + 1, cnt - 1):
            for k in range(j + 1, cnt):
                summ = nums[i] + nums[j] + nums[k]
                if (bucket[summ] == 1):
                    # print(summ)
                    answer += 1
    return answer
