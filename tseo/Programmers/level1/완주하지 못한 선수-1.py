participant_1 = ["leo", "kiki", "eden"]
completion_1 = ["eden", "kiki"]
participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion_2 = ["josipa", "filipa", "marina", "nikola"]
participant_3 = ["mislav", "stanko", "mislav", "ana"]
completion_3 = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()  # 참가자들 일단 정렬
    completion.sort()  # 완주자들 일단 정렬
    for p, c in zip(participant, completion):
        if p != c:  # 두 리스트의 원소를 하나씩 비교하여 다른 값이 있다면
            return p  # 완주를 못한 사람이다
    return (
        participant.pop()
    )  # completion 길이만큼 비교해서 모두 다 같다면 participant에 남은 사람이 완주 못한 사람


print(solution(participant_1, completion_1))
print(solution(participant_2, completion_2))
print(solution(participant_3, completion_3))
