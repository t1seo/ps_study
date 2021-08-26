def print_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    print("=" * 10)


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):  # 0 ~ 3: 각 열을 의미
            # 이전 행에서 j열(현재 위치의 열)을 빼고의 max 값을 더해준다
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1 :])
        print_array(land)  # 확인 용
    return max(land[-1])  # 맨 마지막 행에서 최대값 반환


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

print(solution(land))
