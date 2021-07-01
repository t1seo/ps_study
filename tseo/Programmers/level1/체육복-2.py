n_1 = 5
lost_1 = [2, 4]
reserve_1 = [1, 3, 5]

n_2 = 5
lost_2 = [2, 4]
reserve_2 = [1]

n_3 = 3
lost_3 = [3]
reserve_3 = [1]


def solution(n, lost, reserve):
    # 리스트 컴프리헨션으로 reserve와 lost 리스트 구한다
    real_reserve = [p for p in reserve if p not in lost]
    real_lost = [p for p in lost if p not in reserve]

    for i in real_reserve:
        if i - 1 in real_lost:
            real_lost.remove(i - 1)
        elif i + 1 in real_lost:
            real_lost.remove(i + 1)
    return n - len(real_lost)


print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))
