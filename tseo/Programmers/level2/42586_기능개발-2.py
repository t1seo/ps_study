def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
        print(Q)
    return [q[1] for q in Q]


p1 = [93, 30, 55]
s1 = [1, 30, 5]
p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]

# print(solution(p1, s1))
print(solution(p2, s2))
