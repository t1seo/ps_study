a, b, v = map(int, input().split())
d = (v - b) / (a - b)
if d > int(d):
    d += 1
print(int(d))

# a * d - b * (d - 1) > v

# https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4
"""
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
"""

# // : / - %
# int(d) == (v - b) // (a - b)
