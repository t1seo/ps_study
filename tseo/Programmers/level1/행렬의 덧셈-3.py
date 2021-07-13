arr1_1 = [[1, 2], [2, 3]]
arr2_1 = [[3, 4], [5, 6]]

arr1_2 = [[1], [2]]
arr2_2 = [[3], [4]]


import numpy as np


def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))
print(len(arr1_1))
print(len(arr2_1[0]))
