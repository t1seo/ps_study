import string


"""
n: 진법
t: 미리 구할 숫자의 갯수
m: 게임에 참가하는 인원
p: 튜브의 순서
"""


def solution(n, t, m, p):
    # 진법 변환
    tmp = string.digits + string.ascii_lowercase

    def convert(num, base):
        q, r = divmod(num, base)
        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]

    answer = ""
    candidate = []

    # 각 참여자의 모든 턴에 대한 답
    for i in range(t * m):  # t(미리 구할 숫자) * m(참가 인원 수) = 모든 턴
        conv = convert(i, n)
        for c in conv:
            candidate.append(c)

    # 튜브의 답안 추출
    for i in range(p - 1, t * m, m):  # 배열이 0부터 시작하니 시작은 (튜브의 시작 턴 - 1)
        answer += candidate[i]

    print("candidate: ", candidate)

    return answer


print(solution(2, 4, 2, 1))
