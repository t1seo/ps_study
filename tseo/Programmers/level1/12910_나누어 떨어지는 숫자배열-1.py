def solution(arr, divisor):
    answer = []

    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


arr = [2, 36, 1, 3]
divisor = 11

print(solution(arr, divisor))
