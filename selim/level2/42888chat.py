# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방

def solution(record):
    answer = []
    users = {} # uid : nickname
    for i in range(len(record)):
        record[i] = record[i].split()
        status = record[i][0]
        uid = record[i][1]
        if status == 'Enter' or status == 'Change': # 유저 이름 업데이트
            users[uid] = record[i][2]
    for i in range(len(record)):
        status = record[i][0]
        uid = record[i][1]
        if status == 'Enter':
            answer.append(users[uid]+"님이 들어왔습니다.")
        elif status == 'Leave':
            answer.append(users[uid]+"님이 나갔습니다.")
    return answer