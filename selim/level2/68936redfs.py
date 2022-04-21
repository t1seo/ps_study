answer = [0, 0]
def oneorzero(arr, y0, x0, lenn):
    temp = [0, 0]
    half = int(lenn/2)
    for i in range(y0, y0+half):
        for j in range(x0, x0+half):
            temp[arr[i][j]] += 1
    return temp
    

def check_(arr, y0, x0, lenn):
    if lenn == 1:
        answer[arr[y0][x0]] += 1
        return 
    # check 사분면
    half = int(lenn/2)
    temp = oneorzero(arr, y0, x0, lenn)
    if temp[0] == half * half :
        answer[0] += 1
    elif temp[1] == half * half:
        answer[1] += 1
    else : 
        check_(arr, y0, x0, half)
    temp = oneorzero(arr, y0 + half, x0, lenn)
    if temp[0] == half * half :
        answer[0] += 1
    elif temp[1] == half * half:
        answer[1] += 1
    else : 
        check_(arr, y0 + half, x0, half)
    temp = oneorzero(arr, y0, x0 + half, lenn)
    if temp[0] == half * half :
        answer[0] += 1
    elif temp[1] == half * half:
        answer[1] += 1
    else : 
        check_(arr, y0, x0 + half, half)
    temp = oneorzero(arr, y0+half, x0+half, lenn)
    if temp[0] == half * half :
        answer[0] += 1
    elif temp[1] == half * half:
        answer[1] += 1
    else : 
        check_(arr, y0+half, x0+half, half)
        

def solution(arr):
    lenn = len(arr)
    y0, x0 = 0, 0
    summ = 0
    for i in arr:
        summ += sum(i)
    if summ == lenn * lenn: 
        return [0, 1]
    if summ == 0:
        return [1, 0]
    check_(arr, y0, x0, lenn)
    return (answer)