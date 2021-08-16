def solution(n):
    curr, next = 0, 1
    for _ in range(n):
        curr, next = next, curr + next
    return curr % 1234567
