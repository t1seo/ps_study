def solution(nums):
    type_num = len(set(nums))  # 중복되지 않은 폰켓몬 수를 구한다

    if len(nums) // 2 > type_num:  # 고를 수 있는 수가 폰켓몬 종류보다 많으면
        return type_num  # 폰켓몬 종류만큼 리턴
    else:
        return len(nums) // 2


n1 = [3, 3, 3, 2, 2, 4]
n2 = [3, 3, 3, 2, 2, 2]
print(solution(n2))
