def solution(n):
    l = list(str(n))[::-1]

    return list(map(int, l))


print(solution(12345))
