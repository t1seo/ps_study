"""
https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/
"""


def solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i is 0])

