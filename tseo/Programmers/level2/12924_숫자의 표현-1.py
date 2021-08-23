def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum_result = 0
        for j in range(i, n + 1):  # i번째부터 순서대로 더해준다
            sum_result += j
            if sum_result == n:  # 합이 n인 경우가 나오면
                answer += 1
                break
            elif sum_result > n:
                break
    return answer
