def solution(n):
    sieve = [False, False] + [True] * (n - 1)  # 0과 1은 False
    primes = []

    for i in range(2, n + 1):
        if sieve[i]:  # i가 소수인 경우
            primes.append(i)
            for j in range(2 * i, n + 1, i):  # i 이후 i 배수들을 False
                sieve[j] = False

    return len(primes)


print(solution(10))
print(solution(5))
