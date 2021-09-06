arr_1 = [9, 20, 28, 18, 11]
arr_2 = [30, 1, 21, 17, 28]

arr_3 = [46, 33, 33, 22, 31, 50]
arr_4 = [27, 56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, "0")
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        answer.append(a12)
    return answer
