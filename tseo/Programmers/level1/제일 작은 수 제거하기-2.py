def solution(mylist):
    return [i for i in mylist if i > min(mylist)]


my_list = [4, 3, 2, 1]
print("결과 {} ".format(solution(my_list)))

