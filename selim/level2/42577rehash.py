# https://programmers.co.kr/learn/courses/30/lessons/42577
# 해시
def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    numDict = {phone_book[0]:1}
    maxlen = len(phone_book[0])
    for item in phone_book:
        for i in range(1, len(item)):
            if i <= maxlen : 
                if item[:i] in numDict : 
                    return False 
        numDict[item] = 1
        maxlen = max(len(item), maxlen)
    return True
