def checker(n):
    pre = -1
    diff = 1000
    for i in n:
        if pre == -1:
            pre = int(i)
            continue
        if diff == 1000:
            diff = int(i) - pre
        else:
            if diff != int(i) - pre:
                return 0
        pre = int(i)
    return 1


n = int(input())
count = 0
for i in range(1, n + 1):
    if checker(str(i)):
        count += 1
print(count)

# https://roseline124.github.io/algorithm/2019/03/29/Algorithem-baekjoon-1065.html
"""
num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1

    else :
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1
"""

# https://www.acmicpc.net/source/8789313
"""
print(sum((x//100+x%10==x//10%10*2)|(x<100) for x in range(1,int(input())+1)))
"""
# n % 10 + n // 100 == 2 * (n // 10 % 10)
# 등차수열에서 a1 + a3 = 2 * a2임을 이용
