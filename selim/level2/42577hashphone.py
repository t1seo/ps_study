# https://programmers.co.kr/learn/courses/30/lessons/42577
# 해시 > 전화번호 목록 

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(0, len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False 
    return answer

# def solution1(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=len)
#     # print(phone_book)
#     for i, item in enumerate(phone_book):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j][:len(item)] == item: 
#                 # print(item)
#                 return False 
#     return answer

# testcase 모두 성공하지만 효율성 3 4 에서 fail.. -> 바로 뒤만 검사해서 통과 
# 테스트 3
# 입력값 〉	["12", "123", "1235", "567", "88"]
# 기댓값 〉	false
# 실행 결과 〉	테스트를 통과하였습니다.
# 출력 〉	['12', '123', '1235', '567', '88']