def change_time(time_default = None):	
	try:
		if int(time_default[0]) > 23 or int(time_default[1]) > 59 or int(time_default[2]) > 59:
			return 'Time input is incorrect, values are too big' 
	except Exception as e:
		#print("Oops!", e.__class__, "occurred.")
		if e.__class__ == ValueError:
			return 'Only numbers allowed'
		return 'Check your input!'		
	seconds = int(time_default[0])*3600 + int(time_default[1])*60 + int(time_default[2])
	seconds_dec = seconds*1.15740740741
	if seconds_dec - int(seconds_dec) > 0.5:
		seconds_dec += 1 
	return 'Decimal time: {}:{}:{}'.format(int(seconds_dec//10000), int((seconds_dec%10000)//100), int(seconds_dec%10000)%100)

if __name__=="__main__":
	print('Enter time in format 5 10 10 where 5, 10, 10 are the numbers of hours, minutes, seconds respectively. Split numbers with one space and start input with number.')
	time_default = input().split(' ')
	print(change_time(time_default))
	