# https://programmers.co.kr/learn/courses/30/lessons/67256
# 2020 카카오인턴십 > 키패드 누르기

def solution(numbers, hand):
    answer = ''
    # initial
    hands = {'left':(3,0), 'right':(3,2)}
    dist = [(3,1)]
    for i in range(3):
        for j in range(3):
            dist.append((i, j))
    if hand == 'left':
        c = 'L'
    else:
        c = 'R'
    
    for i, item in enumerate(numbers):
        if item in [1,4,7]:
            hands['left'] = dist[item]
            answer += 'L'
        elif item in [3,6,9]:
            hands['right'] = dist[item] 
            answer += 'R'
        else:
            fromleft = abs(hands['left'][0] - dist[item][0]) + abs(hands['left'][1] - dist[item][1])
            fromright = abs(hands['right'][0] - dist[item][0]) + abs(hands['right'][1] - dist[item][1])
            # print(fromleft, fromright, dist[item])
            if fromleft < fromright:
                hands['left'] = dist[item]
                answer += 'L'
            elif fromleft > fromright:
                hands['right'] = dist[item]
                answer += 'R'
            else:
                hands[hand] = dist[item]
                answer += c
        # print(hands)
    # print(answer)
    return answer