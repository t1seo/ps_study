# https://programmers.co.kr/learn/courses/30/lessons/17686
# 2018 KAKAO BLIND RECRUITMENT > [3차] 파일명 정렬

def solution(files):
    answer = []
    
    # parsing 
    newfiles = []
    for x, file in enumerate(files):
        st, mid, end = '', '', ''
        nothead = 0
        for i in range(len(file)):
            if file[i].isdigit():
                mid += file[i]
                nothead = 1
            elif nothead == 0:
                st += file[i]
            else:
                end += file[i:]
                break
        # newfiles.append((file[:st], file[st:end], file[end:]))
        newfiles.append((st, mid, end))
    newfiles.sort(key=lambda x: (x[0].upper(), int(x[1])))
    # print(newfiles)
    return [''.join(x) for x in newfiles]