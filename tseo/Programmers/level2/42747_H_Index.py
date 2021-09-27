def solution(citations):
    citations.sort()
    n = len(citations)  # 전체 발표된 논문 개수

    for i in range(n):
        if citations[i] >= n - i:  # 인용된 논문 개수 = 발표된 논문 개수(전체 - i) 일치하는 지점 찾기
            return n - i
    return 0


citations = [3, 0, 6, 1, 5]

print(solution(citations))
