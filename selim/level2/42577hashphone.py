# https://programmers.co.kr/learn/courses/30/lessons/42577
# 해시 > 전화번호 목록 

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book) 	# 길이 정렬이 아닌 맨 앞 숫자대로 정렬 
    for i in range(0, len(phone_book) - 1): 
		# 그 결과 바로 뒤에만 확인하면 된다. 
		# 바로 뒤 숫자에서 접두사가 성립하지 않으면 그 뒤는 더더욱 확인할 필요가 없음 왜냐하면 앞에 숫자대로 정렬했기 때문에. 
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False 
    return answer

# def solution1(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=len) # 길이가 긴 순서대로 정렬한 후 
#     # print(phone_book)
#     for i, item in enumerate(phone_book):		# 뒤에 번호들을 모두 확인했지만 효율성 테스트에서 fail 
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