from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)

    answer = []
    time = 0  # 경과 시간
    count = 0  # 작업 완료 개수

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:  # 목록의 맨 앞의 것이 완료되면
            progresses.popleft()  # 맨 앞 작업 pop
            speeds.popleft()  # 맨 앞 작업의 속도 pop
            count += 1  # 작업 완료 개수 증가
        else:  # 완료된 작업이 없다면 시간 증가
            if count > 0:  # 이전까지 완료된 것을 모두 answer에 append
                answer.append(count)
                count = 0
            time += 1  # 경과 시간 증가

    answer.append(count)  # 마지막으로 count를 append
    return answer

