arr_1 = 10
arr_2 = 12
arr_3 = 11
arr_4 = 13


def solution(n):
    return n % sum([int(c) for c in str(n)]) == 0


print(solution(arr_1))
print(solution(arr_2))
print(solution(arr_3))
print(solution(arr_4))
