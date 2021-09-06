def solution(N, stages):
    k = len(stages)
    s = []  # 실패율 리스트

    for i in range(1, N + 1):
        c = 0  # c: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수
        for j in range(len(stages)):
            if stages[j] == i:
                c += 1
        if c == 0:
            s.append(0)
        else:
            s.append(c / k)
        k = k - c  # k: 스테이지에 도달한 플레이어 수

    a = sorted(s, reverse=True)  # 스테이지 실패율 내림차순 정렬
    answer = []

    # 리스트 a의 값이 리스트 s의 어느 위치에 있는지 값을 확인해 answer에 저장한다.
    for i in range(len(a)):
        answer.append(s.index(a[i]) + 1)
        s[s.index(a[i])] = 2  # 리스트 s의 값을 2로 바꿔준다

    return answer
