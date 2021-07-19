def get_gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x


def solution(n, m):
    answer = []
    gcd = get_gcd(n, m)
    lcm = (n * m) // gcd

    answer.append(gcd)
    answer.append(lcm)

    return answer
