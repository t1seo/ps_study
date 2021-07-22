c = int(input())
for i in range(0, c):
	n = list(map(int, input().split()))
	score = 0
	students = 0
	for j in range(0, n[0]):
		score += n[j + 1]
	score = score / n[0]
	for k in range(0, n[0]):
		if n[k + 1] > score:
			students += 1
	print('%.3f%%'%(students * 100 / n[0]))

# https://ooyoung.tistory.com/62
'''
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
'''

# for i in range(0, c):
# ==
# for _ in range(c):

# sum(list)
# list[1:] : index 1 ~ last

# print(f'blahblah{expression}')
# format string literal (f-strings) : f for prefix
# better readability than %-formatting(in my code)
