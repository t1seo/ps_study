answer = [0]
def dfs(numbers, target, curr_lev, fin_lev, summ):
    if curr_lev == fin_lev:
        if summ == target:
            answer[0] += 1
        return 
    dfs(numbers, target, curr_lev+1, fin_lev, summ + numbers[curr_lev])
    dfs(numbers, target, curr_lev+1, fin_lev, summ - numbers[curr_lev])

def solution(numbers, target):
    dfs(numbers, target, 0, len(numbers), 0)
    return(answer[0])