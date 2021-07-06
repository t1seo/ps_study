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
    # 여벌 체육복을 도난 당했을 수 있으므로 전처리 해준다
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # 왼쪽 학생 먼저 빌려주고, 만약 있다면 오른쪽 학생을 빌려준다
    for i in set_reserve:
        if i - 1 in set_lost:  # 앞의 학생에게 빌려준다
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:  # 뒤의 학생에게 빌려준다
            set_lost.remove(i + 1)

    return n - len(set_lost)


print(solution(n_1, lost_1, reserve_1))
print(solution(n_2, lost_2, reserve_2))
print(solution(n_3, lost_3, reserve_3))
