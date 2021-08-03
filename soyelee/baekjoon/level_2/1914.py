def recur(n, frm, to):
    if n > 1:
        recur(n - 1, frm, 6 - frm - to)
    print(frm, to)
    if n > 1:
        recur(n - 1, 6 - frm - to, to)


n = int(input())
print(2 ** n - 1)
if n <= 20:
    recur(n, 1, 3)

# https://sung-jun.tistory.com/110
# 6 : sum of each pole's number
