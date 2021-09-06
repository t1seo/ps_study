def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))
