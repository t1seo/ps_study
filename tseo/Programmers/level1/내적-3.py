a_1 = [1, 2, 3, 4]
b_1 = [-3, -1, 0, 2]

a_2 = [-1, 0, 1]
b_2 = [1, 0, -1]


def solution(a, b):
    # print(list(map(lambda i: a[i] * b[i], range(len(a)))))
    return sum(map(lambda i: a[i] * b[i], range(len(a))))


print(solution(a_1, b_1))
print(solution(a_2, b_2))
