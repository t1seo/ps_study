arr_1 = 10
arr_2 = 12
arr_3 = 11
arr_4 = 13


def solution(x):
    num_sum = sum(list(map(int, list(str(x)))))
    if x % num_sum:
        return False
    else:
        return True


print(solution(arr_1))
print(solution(arr_2))
print(solution(arr_3))
print(solution(arr_4))
