def change_time(time_default = None):	
	try:
		if int(time_default[0]) > 9 or int(time_default[1]) > 99 or int(time_default[2]) > 99:
			return 'Time input is incorrect, values are too big' 
	except Exception as e:
		#print("Oops!", e.__class__, "occurred.")
		if e.__class__ == ValueError:
			return 'Only numbers allowed'
		return 'Check your input!'			
	seconds = int(time_default[0])*10000 + int(time_default[1])*100 + int(time_default[2])
	seconds_dec = seconds*0.864
	if seconds_dec - int(seconds_dec) > 0.5:
		seconds_dec += 1 
	return 'Normal time: {}:{}:{}'.format(int(seconds_dec//3600), int((seconds_dec%3600)//60), int(seconds_dec%3600)%60)

if __name__=="__main__":
	print('Enter time in format 5 90 10 where 5, 10, 10 are the numbers of decimal hours, minutes, seconds respectively. Split numbers with one space and start input with number.')
	time_default = input().split(' ')
	print(change_time(time_default))
	