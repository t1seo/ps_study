from itertools import combinations


# 소수 판별 함수
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    # 서로 다른 3개의 숫자를 뽑아서 리스트로 만들어준다
    n_list = list(combinations(set(nums), 3))

    for n in n_list:
        if is_prime(sum(n)):  # 각 3개의 숫자의 합이 소수인지 판별
            answer += 1

    return answer


nums_2 = [1, 2, 7, 6, 4]

print(solution(nums_2))
