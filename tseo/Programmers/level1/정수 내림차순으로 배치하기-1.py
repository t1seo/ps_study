def solution(n):
    l = sorted(str(n), reverse=True)
    return int("".join(l))


print(solution(118372))
