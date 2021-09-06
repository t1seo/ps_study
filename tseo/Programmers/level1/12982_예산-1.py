from itertools import accumulate


def solution(b, budget):
    b.sort()  # 부서별 금액을 정렬
    sum_list = list(accumulate(b))  # 누적합 리스트
    # print(sum_list)

    i = 0
    while i < len(sum_list):
        if sum_list[i] > budget:
            return i
        i += 1
    return i


d_1 = [1, 3, 2, 5, 4]
d_2 = [2, 2, 3, 3]

print(solution(d_1, 9))
print(solution(d_2, 10))

