arr_1 = [9, 20, 28, 18, 11]
arr_2 = [30, 1, 21, 17, 28]

arr_3 = [46, 33, 33, 22, 31, 50]
arr_4 = [27, 56, 19, 14, 14, 10]

from collections import deque


# ['1', '0', '1', '0', '1'] => # # #
def decode_row(row):
    decoded_row = []
    for box in row:
        if box == "1":
            decoded_row.append("#")
        else:
            decoded_row.append(" ")
    return "".join(decoded_row)


def solution(n, arr_1, arr_2):

    answer = []
    for i in range(n):
        # OR 연산 -> 2진법으로 바꾸기 -> 리스트로 바꾼 후 앞의 0b 제외
        or_result = list(bin(arr_1[i] | arr_2[i]))[2:]
        # 예) 111 -> 00111
        i = len(or_result)
        while i < n:
            dq = deque(or_result)
            dq.appendleft(0)
            i += 1
            or_result = list(dq)
        answer.append(decode_row(or_result))

    return answer


print(solution(5, arr_1, arr_2))
print(solution(6, arr_3, arr_4))
