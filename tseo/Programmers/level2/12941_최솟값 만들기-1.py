def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0

    for a, b in list(zip(A, B)):
        answer += a * b

    return answer


# A = [1, 4, 2]
# B = [5, 4, 4]
A = [1, 2]
B = [3, 4]
print(solution(A, B))
