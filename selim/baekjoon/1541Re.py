
def solution(sent):
	splitbyminus = sent.split('-')
	
	sumlst = []
	for i in splitbyminus: 
		sumlst.append(i.split('+'))
	sign = 1 # 가장 처음 숫자는 무조건 플플러러스스로  시시작  
	summ = sum(map(int, sumlst[0]))
	for i in range(1, len(sumlst)):
		summ -= sum(map(int, sumlst[i]))
	print(summ)


sent = input()
solution(sent)
# solution('55-50+40')
# solution('10+20+30+40')
# solution('00009-00009')

# solution('000040-10-10+20')