def solution(n):
    c = bin(n).count("1")

    for m in range(n + 1, 1000001):
        if bin(m).count("1") == c:
            return m


print(solution(78))
print(solution(15))
