# https://programmers.co.kr/learn/courses/30/lessons/42860
# 탐욕법(Greedy) > 조이스틱 

def setMoves(name):
    moves = []
    upkey = 	{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12}
    downkey = 	{0: 0, 'Z': 1, 'Y': 2, 'X': 3, 'W': 4, 'V': 5, 'U': 6, 'T': 7, 'S': 8, 'R': 9, 'Q': 10, 'P': 11, 'O': 12, 'N': 13}
    for i in name:
        if i in upkey:
            moves.append(upkey[i])
        else : 
            moves.append(downkey[i])
    return moves

def solution(name):
    moves = setMoves(name) # "JAN" -> [9, 0, 13]
    # print(moves)
    pos = 0
    answer = 0
    while True:
        answer += moves[pos] # answer += 9
        moves[pos] = 0 # [0, 0, 13]

        if sum(moves) == 0: break

        left = 1
        right = 1

        while moves[pos - left] == 0: # 1
            left += 1

        while moves[pos + right] == 0: # 2
            right += 1

        if left >= right: # 1 >= 2 (x)
            pos += right
            answer += right

        else:             # 1(left) <= 2(right) (o)
            pos -= left     # 0 -= 1
            answer += left  # 9(answer) += 1
    
    # while문이 끝나면 answer return 
    return answer



"""
"JEROEN", 56
"JAN", 23
"JAZ", 11
"ABAAAAAAAAABB", 7
"""