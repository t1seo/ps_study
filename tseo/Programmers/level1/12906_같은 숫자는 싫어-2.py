def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in arr:
        if answer[-1] != i:
            answer.append(i)

    return answer


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))
