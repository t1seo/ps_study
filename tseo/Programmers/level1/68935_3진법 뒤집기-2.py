def solution(n):
    tmp = ""
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


print(solution(45))
print(solution(125))
