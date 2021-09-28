def solution(brown, yellow):
    s = brown + yellow  # 총 블럭 개수
    for width in range(s, 2, -1):  # 블록의 가로
        if s % width == 0:
            height = s // width  # 블록의 높이
            if yellow == (width - 2) * (height - 2):
                return [width, height]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
