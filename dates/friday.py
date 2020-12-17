def fridays(usual = True):
	if usual:
		days = [31,28,31,30,31,30,31,31,30,31,30,31]
		total = 365
	else:
		days = [31,29,31,30,31,30,31,31,30,31,30,31]
		total = 366
	friday13s = []	
	week = {'m':'t','t':'w','w':'th','th':'f','f':'s','s':'su','su':'m'}
	for key in week:	
		days_of_the_week = [key]	
		for i in range(total-1):	
			days_of_the_week.append(week[days_of_the_week[i]])
		counter = 0	
		for month in days:
			for day in range(month):
				days_of_the_week[counter] = days_of_the_week[counter] + str(day+1)
				counter += 1 
		friday13s.append(days_of_the_week.count('f13'))
	return('Minimum number of friday 13s:{} \nMaximum number of friday 13s:{}'.format(min(friday13s),max(friday13s)))			
def input_handler():
	print('Enter U to count fridays in usual year or L to count fridays in leap year')
	data = input()
	if data == 'U' or data == 'u':
		print(fridays())
		return 0
	elif data == 'L' or data == 'l':
		print(fridays(False))
		return 0
	else:
		return input_handler()	 	


if __name__=="__main__":
	input_handler()		
