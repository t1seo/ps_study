# https://programmers.co.kr/learn/courses/30/lessons/87377
# 위클리 챌린지 > 10주차_교점에 별 만들기

def getIpoints(line):
    ipointlst = []
    answer = ''
    x, y = 0, 0
    # try and except ZeroDivisionsPoints
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            try: 
                upper = (line[i][1]*line[j][2]) - (line[i][2]*line[j][1])
                lower = (line[i][0]*line[j][1]) - (line[i][1]*line[j][0])
                x = upper / lower
            except (ZeroDivisionError):
                x = 'err'
                pass
            if (x == 'err'):
                continue
            try : 
                upper = (line[i][2]*line[j][0] - line[i][0]*line[j][2])
                lower = (line[i][0]*line[j][1]) - (line[i][1]*line[j][0])
                y = upper / lower
            except (ZeroDivisionError):
                y = 'err'
                pass
            if (y == 'err'):
                continue
                
            # delete float numbers
            if (x != int(x)):
                continue
            if (y != int(y)):
                continue
            ipointlst.append((x, y))
    # delete duplicate numbers
    
    ipointlst = list(set(ipointlst))
    
    for i, item in enumerate(ipointlst):
        temp = [int(item[0]), int(item[1])]
        ipointlst[i] = temp
    ipointlst.sort()
    return ipointlst
        

def solution(line):
    # 교점 구하기 getIpoints
    ipointlst = getIpoints(line)
    print(ipointlst)
    
    if len(ipointlst) == 1: # 별은 적어도 한 개 그려진다 
        return ["*"]
    
    # set four points 
    leftX, rightX, highY, lowY = ipointlst[0][0], ipointlst[0][0], ipointlst[0][1], ipointlst[1][1]
    
    for ind, item in enumerate(ipointlst):
        print(ind, item)
        if item[0] < leftX:
            leftX = item[0]
        if item[0] > rightX:
            rightX = item[0]
        if item[1] > highY:
            highY = item[1]
        if item[1] < lowY : 
            lowY = item[1]
    # print(leftX, rightX, highY, lowY )
    result = []
    for i in range(highY-lowY+1):
        result.append("."*(rightX-leftX+1))
    for i, item in enumerate(ipointlst):
        
        newx = item[0] - leftX
        newy = -(item[1] - highY)
        
        newstr = result[newy][:newx] + '*' + result[newy][newx+1:]
        # print(newstr)
        result[newy] = newstr
        
    # print(result)
    return result
    
    
# 참고사항을 안 읽어서 직접 구함... 끝까지 읽자 
# def solution1(line): # line은 이중 배열 
#     ipointlst = []
#     newline = []
#     for i in range(len(line)):
#         newi = []
#         if line[i][1] != 0:
#             for x in line[i]:
#                 if (x != 0):
#                     newi.append(x / line[i][1])
#                 else:
#                     newi.append(0)
#             newline.append(newi)
#         else:
#             newline.append(line[i])
#     print(newline)
#     x, y = 0, 0
#     for i in range(len(line)-1):
#         for j in range(i+1, len(line)):
#             if (line[i][1] == 0 and line[j][1] == 0):
#                 continue
#             elif (line[i][1] == 0):
#                 x = -line[i][2]
#                 y = -(x*newline[j][0] + newline[i][2])
#             elif (line[j][1] == 0):
#                 x = -line[j][2]
#                 y = -(x*newline[i][0] + newline[i][2])
#             else:
#                 a = newline[i][0] - newline[j][0]
#                 c = newline[i][2] - newline[j][2]
#                 if (a == 0):
#                     continue # 평행
#                 elif (c == 0):
#                     x = 0
#                 else:
#                     x = (-c)/a
#                 y = -(x*newline[i][0] + newline[i][2])
#             print(i, j)
#             ipointlst.append([x, y])
            
#     print(ipointlst)
            
#     answer = []
#     return answer

"""
모범코드

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
def solution(line):
    points = set()
    maxX, maxY, minX, minY = -10e10, -10e10, 10e10, 10e10
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            tmp = A * D - B * C
            if tmp != 0 and (B*F-E*D)%tmp == 0 and (E*C-A*F)%tmp == 0:
                X, Y = (B*F-E*D)//tmp, (E*C-A*F)//tmp
                maxX, maxY, minX, minY = max(maxX, X), max(maxY, Y), min(minX, X), min(minY, Y)
                points.add((X, Y))
    answer = [["." for c in range(maxX-minX+1)] for r in range(maxY-minY+1)]
    for x, y in points:
        answer[maxY-y][x-minX] = "*"
    return ["".join(row) for row in answer]
"""