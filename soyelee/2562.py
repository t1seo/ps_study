maximum = 0;
index = 0;
for i in range(0, 9):
	n = int(input())
	if maximum < n:
		maximum = n
		index = i + 1
print(maximum)
print(index)

# https://claude-u.tistory.com/104
'''
num_list = []
for i in range(9):
	num_list.append(int(input()))
print(max(num_list))
print(num_list.index(max(num_list))+1)
'''

# num_list = []
# ==
# num_list = list()

# append - add new item at the end of list

# index - show the index of certain item (only the first one)
