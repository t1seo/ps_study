def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length  # 다리 길이만큼 0으로 초기화한 큐

    while q:
        time += 1  # 경과 시간
        q.pop(0)  # 다리 위엑서 맨 앞에 있는 것 pop
        if truck_weights:  # 트럭이 남아 있다면
            if sum(q) + truck_weights[0] <= weight:  # 다리 위의 트럭 무게와 다리에 들어갈 트럭 무게 합
                q.append(truck_weights.pop(0))
            else:
                q.append(0)  # 트럭이 안들어가면 0을 append
    return time


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge_length, weight, truck_weights))
