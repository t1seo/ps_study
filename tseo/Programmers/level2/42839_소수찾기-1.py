import math
from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    k = math.sqrt(n)

    if n < 2:
        return False

    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    prime_list = []

    for k in range(1, len(numbers) + 1):
        # 숫자들의 모든 조합을 리스트로 만들어낸다
        permu_list = list(map("".join, permutations(list(numbers), k)))

        # 중복도 있으니 set으로 유일한 것들만 다룬다
        for n in list(set(permu_list)):
            if is_prime(int(n)):  # 소수인지 판별
                prime_list.append(int(n))

    # 최종적으로 소수 개수만 리턴
    answer = len(set(prime_list))
    return answer


print(solution("011"))
