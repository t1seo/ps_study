"""
https://www.acmicpc.net/problem/1541
잃어버린 괄호 
"""
import re

exprs = input()

numlst = list(map(int, exprs.replace('+', ' ').replace('-', ' ').split()))
# print(numlst)
lenn = len(numlst)
summ = numlst[0]
op_ind = 0
oplst = []
for i in range(len(exprs)):
	if (exprs[i] == '-' or exprs[i] == '+'):
		oplst.append(exprs[i])
# print(oplst)
while (op_ind < lenn - 1): # 0 < 2
	if oplst[op_ind] == '-': # op[0] == '-'
		op_ind += 1 # 1 
		temp = numlst[op_ind] # numlst[1] = 50
		while (op_ind < lenn-1 and oplst[op_ind] == '+'): # 1 < 2 and oplst[1] == '+'
			op_ind += 1 # op_ind = 2
			temp += numlst[op_ind] # numlst[2] = 40 => 90 
		summ -= temp # 55 - 90
	else :
		op_ind += 1
		summ += numlst[op_ind]
print(summ)

"""
0-101-01
답 : -102
"""