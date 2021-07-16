arr1_1 = [[1, 2], [2, 3]]
arr2_1 = [[3, 4], [5, 6]]

arr1_2 = [[1], [2]]
arr2_2 = [[3], [4]]


def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer


print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))
