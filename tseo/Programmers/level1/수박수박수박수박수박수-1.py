import itertools


def solution(n):
    it = itertools.repeat("수박", n // 2)
    if n % 2 == 0:
        return "".join(list(it))
    else:
        l = list(it)
        l.append("수")
        return "".join(l)


print(solution(3))
print(solution(4))
