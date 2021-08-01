# https://programmers.co.kr/learn/courses/30/lessons/12906
# 연습문제 > 같은 숫자는 싫어

def solution(arr):
    answer = []
    a = arr[0]
    answer.append (a)
    for t in range(1,len(arr)):
        if a != arr[t]:
            answer.append(arr[t])
            a = arr[t]
    return answer

#  arr				answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]		[4,3]
# 처음에는 set()으로 풀려고 했는데 같은 숫자를 모두 제거해서는 안됐다. 
# 따라서 for문 하나를 써서 읽어나가면 같으면 넘기고 다르면 업데이트 하는 식으로 품. 