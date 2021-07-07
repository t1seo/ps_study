numbers_1 = [2, 1, 3, 4, 1]
numbers_2 = [5, 0, 2, 7]


from itertools import combinations


def solution(numbers):
    answer = set()

    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))

    return list(answer)


print(solution(numbers_1))
print(solution(numbers_2))
