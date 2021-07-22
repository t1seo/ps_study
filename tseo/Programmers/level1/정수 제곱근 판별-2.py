import math


def solution(n):
    num = math.sqrt(n)

    if num % 1 == 0:
        return (num + 1) ** 2
    else:
        return -1


print(solution(121))
print(solution(122))
print(solution(3))
