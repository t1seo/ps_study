from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    # queue에 인덱스 값도 같이 넣어준다
    queue.append([numbers[0], 0])  # +number, index=0
    queue.append([-1 * numbers[0], 0])  # -number, index=0

    while queue:
        temp, idx = queue.popleft()
        idx += 1  # index++
        if idx < n:
            queue.append([temp + numbers[idx], idx])  # 숫자 더해준 경우
            queue.append([temp - numbers[idx], idx])  # 숫자 빼준 경우
        else:
            if temp == target:
                answer += 1
    return answer
