numbers_1 = [2, 1, 3, 4, 1]
numbers_2 = [5, 0, 2, 7]


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


print(solution(numbers_1))
print(solution(numbers_2))
