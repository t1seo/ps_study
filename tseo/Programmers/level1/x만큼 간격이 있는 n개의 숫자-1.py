x_1 = 2
n_1 = 5
x_2 = 4
n_2 = 3
x_3 = -4
n_3 = 2


def solution(x, n):
    return [x * i for i in range(1, n + 1)]


print(solution(x_1, n_1))
print(solution(x_2, n_2))
print(solution(x_3, n_3))
