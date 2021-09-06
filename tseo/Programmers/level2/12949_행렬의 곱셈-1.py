import numpy as np


def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = np.dot(arr1, arr2)
    return answer.tolist()


arr1_1 = [[1, 4], [3, 2], [4, 1]]
arr2_1 = [[3, 3], [3, 3]]
arr1_2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))
