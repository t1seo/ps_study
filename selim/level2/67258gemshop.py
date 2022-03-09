# https://programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십 > 보석 쇼핑 [투포인터]
# https://dev-note-97.tistory.com/70 <- Good 

def solution(gems):
    # two pointer prob 
    result = [1, 1]
    categL = len(set(gems))
    # print(categ)
    answer = len(gems) + 1
    st = 0
    ed = 0
    numDict = {}
    while ed < len(gems):
        if gems[ed] in numDict:
            numDict[gems[ed]] += 1
        else:
            numDict[gems[ed]] = 1
        ed += 1
        
        if len(numDict) == categL: # 4 == 4
            while st < ed:
                if numDict[gems[st]] > 1:
                    numDict[gems[st]] -= 1
                    st += 1
                elif ed - st < answer:
                    answer = ed - st
                    result = [st+1, ed]
                    break
                else:
                    break
    print(numDict)
    return result
    
    