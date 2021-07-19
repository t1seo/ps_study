# https://programmers.co.kr/learn/courses/30/lessons/42748
# 정렬 > K번째수

def solution(array, commands):
    answer = []
    for i in range(len(commands)): # 예를 들어 튜플이 (2,5,3)이라 하면 
        newar = array[commands[i][0] - 1:commands[i][1]] # 2번쨰~5번째를 잘라오기 
        newar.sort()									 # 정렬하기 
        answer.append(newar[commands[i][2] - 1])		 # 정렬하고 나온 리스트의 세번째를 answer list에 append
    return answer

# 모범풀이 
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
	
# 	sorted(array[x[0]-1 : x[1]])로 새로운 array를 만들고 sorted까지 
# 	그리고 나온 인자에 [x[2] -1]까지 해서 값 하나만 나오게 한다. 
# 	lambda 이름 없는 함수. lambda 인자 : 표현식 으로 쓰인다 
# 	map(함수, 리스트) x 인자에는 commands 값들이 하나씩 들어간다 
# 	재밌게도 map()바깥에 list()를 안 감싸면 런타임에러가 난다 
# 	map object 라서 그런듯 하다 리스트를 반환하는 줄 알았는데 엄연히 다름 
