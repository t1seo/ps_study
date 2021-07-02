participant_1 = ["leo", "kiki", "eden"]
completion_1 = ["eden", "kiki"]
participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion_2 = ["josipa", "filipa", "marina", "nikola"]
participant_3 = ["mislav", "stanko", "mislav", "ana"]
completion_3 = ["stanko", "ana", "mislav"]

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    # print(answer) # Counter 객체
    # print(answer.keys()) # key(이름)만 뽑는다
    # print(list(answer.keys())) # dict_keys -> list
    # print(list(answer.keys())[0]) # list의 0번째 원소

    return list(answer.keys())[0]


print(solution(participant_1, completion_1))
print(solution(participant_2, completion_2))
print(solution(participant_3, completion_3))
