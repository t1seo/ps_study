a, b = input().split()
if int(a[::-1]) < int(b[::-1]):
    print(int(b[::-1]))
else:
    print(int(a[::-1]))

# slice[start:stop:step]
# [::-1] : reversed string

# reverse	: list type function. no return. Changes the original list
# reversed	: built-in function. return reversed one. (original : unchanged)

# 'separator'.join(reversed(str))
# str -> reversed : list -> Use 'join' to make list to str
