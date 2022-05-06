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

#  https://programmers.co.kr/learn/courses/30/lessons/42888
# 20220504에 다시 품

def solution1(record):
    users = {}
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] == 'Enter' or record[i][0] == 'Change':
            users[record[i][1]] = record[i][2]
    # print(users)
    finalstr = []
    for item in record:
        if item[0] == 'Enter':
            finalstr.append("{}님이 들어왔습니다.".format(users[item[1]]))
        if item[0] == 'Leave':
            finalstr.append("{}님이 나갔습니다.".format(users[item[1]]))
    return(finalstr)