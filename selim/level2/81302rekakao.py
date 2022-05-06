def check(room):
    sign = [[0,1], [0,-1], [-1,0], [1,0]]
    diag = [[1,1], [1,-1], [-1,-1], [-1,1]]
    
    for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    for y, x in sign:
                        newy = y + i
                        newx = x + j
                        if newy >= 5 or newy < 0 or newx >= 5 or newx < 0:
                            continue
                        if room[newy][newx] == 'P':
                            return 0
                        if room[newy][newx] == 'O':
                            checky = 2 * y + i
                            checkx = 2 * x + j
                            if checky >= 5 or checky < 0 or \
                            checkx >= 5 or checkx < 0:
                                continue
                            if room[checky][checkx] == 'P':
                                return 0
                    for y, x in diag:
                        newy = y + i
                        newx = x + j
                        if newy >= 5 or newy < 0 or newx >= 5 or newx < 0:
                            continue
                        if room[newy][newx] == 'P':
                            if room[newy][j] == 'O' or room[i][newx] == 'O':
                                return 0
    return 1
                            
def solution(places):
    answer = []
    for room in places:
        answer.append(check(room))
    return answer