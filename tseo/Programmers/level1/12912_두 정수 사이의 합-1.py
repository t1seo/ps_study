def solution(a, b):
    if b > a:
        n = list(range(a, b + 1))
    else:
        n = list(range(b, a + 1))

    return sum(n)
