import itertools


def solution(n):
    s = "수박" * n
    return s[:n]


print(solution(3))
print(solution(4))
