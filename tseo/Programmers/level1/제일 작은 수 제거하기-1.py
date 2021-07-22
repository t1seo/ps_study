def solution(arr):
    tmp = sorted(arr, reverse=True)
    min_value = tmp.pop()
    arr.remove(min_value)

    if len(arr) > 0:
        return arr
    else:
        return [-1]


print(solution([4, 3, 2, 1]))
print(solution([10]))
