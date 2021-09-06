def solution(array, commands):
    def converter(array, command):
        arr = array[command[0] - 1 : command[1]]  # slicing
        arr = sorted(arr)  # sorting
        return arr[command[2] - 1]  # return k'th number

    answer = []

    for command in commands:
        answer.append(converter(array, command))

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
