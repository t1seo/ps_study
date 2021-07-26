t = int(input())
for _ in range(t):
    r, s = input().split()
    for i in range(len(s)):
        for _ in range(int(r)):
            print(s[i], end="")
    print()

# https://pacific-ocean.tistory.com/41
"""
t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
"""

# https://ooyoung.tistory.com/69
"""
n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김
"""

# print() -> end='\n' is default
