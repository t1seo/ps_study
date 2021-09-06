# https://programmers.co.kr/learn/courses/30/lessons/82612
# 위클리 챌린지 > 부족한 금액 계산하기 lv.1

def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(1, count + 1): # 3 + 6 + 9 + 12가 되는 for 문 
        sum += price * i
    answer = sum - money
    if (answer < 0): # max(0, answer)로 바꿔도 좋을 듯 
        return 0
    return answer

"""
price	money	count	|result
3		20		4		|10
설명
이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면, 
총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 
10만큼 부족하므로 10을 return 합니다.

모범코드 
price*(count+1)*count//2-money 산술평균 이용함 
"""