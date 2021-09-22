# https://programmers.co.kr/learn/courses/30/lessons/12941
# 연습문제 > 최솟값 만들기 

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    lenn = len(A)
    for i in range(lenn):
        answer += A[i] * B[i]
    return answer

# 모범코드 zip  sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
