arr1_1 = [[1, 2], [2, 3]]
arr2_1 = [[3, 4], [5, 6]]

arr1_2 = [[1], [2]]
arr2_2 = [[3], [4]]


import numpy as np


def solution(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
    return (A + B).tolist()


print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))
