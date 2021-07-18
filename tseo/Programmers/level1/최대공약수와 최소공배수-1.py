import math


def solution(n, m):
    answer = []
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd

    answer.append(gcd)
    answer.append(lcm)

    return answer
