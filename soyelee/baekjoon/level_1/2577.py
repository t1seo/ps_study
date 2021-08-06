a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
count = [0] * 10
while abc != 0:
    n = abc % 10
    abc = int(abc / 10)
    count[int(n)] += 1
for i in range(0, 10):
    print(count[i])

# https://pacific-ocean.tistory.com/34
"""
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))
"""

# str.count(chr) : count the number of 'chr' in list 'str'

# https://sssunho.tistory.com/29
"""
i=input;a=i()*i()*i()
for i in range(10):print`a`.count(`i`)
"""
