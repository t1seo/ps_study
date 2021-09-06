# https://programmers.co.kr/learn/courses/30/lessons/42746
# 정렬 > 가장 큰 수 

def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : (x*4), reverse = True) 
    strr = ""
    for t in num:
        strr += t
    return str(int(strr))
    # return str(int(''.join(num)))

# 참고: https://wooaoe.tistory.com/82 [개발개발 울었다]
"""
모범코드 요지는 원소가 1000이하 값이므로 모든 값을 4의 길이로 만든 후 비교하는 것 
ex) 12 -> 1212 (:4로 인해 뒤에 1212생략)
ex) 123 -> 1231 (:4로 인해 뒤에 23123123생략)
ex) 0 -> 0000 (*4한 결과)

이렇게 하고 [:4]로 4의 길이만 비교. 
그리고 큰 값이 앞에 오도록 reverse=True를 적용해서 정렬 

그다음에는 str을 다 이어주고 return 해주면 된다. 
return str(int(''.join(num))) 이걸로 해야 더 빠름 
return strr (fail test11)
return str(int(strr)) (ok)
"""

# def solution(numbers):
#     numbers.sort(key=str, reverse=True)
#     for i in range(len(numbers) - 1):
#         if str(numbers[i])[0] != str(numbers[i + 1])[0]:
#             continue
#         elif str(numbers[i])[:-1] == str(numbers[i + 1]):
#             # print('a')
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#         # print(str(numbers[i])[-1], str(numbers[i])[:-1]== str(numbers[i + 1]))
#     # print(numbers)
#     strr = ""
#     for t in numbers:
#         strr += str(t)
#     return strr

# def solution(numbers):
#     answer = ''
#     bucket = [[]] * 10
#     for i in numbers:
#         tmp = str(int(i))
#         c = int(tmp[0])
#         tmpli = bucket[c]
#         print(bucket[c])
#         tmpli.append(tmp)
#         # insrt_tmp(bucket, tmp)
#     print(bucket)
        
#     print(str(int(numbers[0])))
#     return answer
