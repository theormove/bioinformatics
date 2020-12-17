TEMPERATURE = 100
COEFFICIENT = 0.5
def time_passage(material, temperature, coef): #calculates temperature values in list after passing 1 time unit
	length = len(material)
	new_material = []
	for i in range(length):
		new_material.append(0)
	for coord in range(length):
		if coord > 0 and coord < (length-1):
			new_material[coord] = material[coord] + coef*(material[coord-1]-2*material[coord]+material[coord+1])
		if coord == 0:
			new_material[coord] = material[coord] + coef*(-material[coord]+material[coord+1])
		if coord == length-1:
			new_material[coord] = material[coord] + coef*(material[coord-1]-material[coord])
	new_material[int(length/2)] = temperature
	return new_material					
						
def interactive(): #asks user length of the list and time to pass
	print('Enter X')
	try:
		x = int(input())
	except:
		print('Invalid X')
		return interactive()
	print('Enter T')
	try:
		time = int(input())
	except:
		print('Invalid T')
		return interactive()
	material = []	
	for i in range(x):
		material.append(0)
	material[int(x/2)] = TEMPERATURE
	print(material)	
	for t in range(time):
		material = time_passage(material,TEMPERATURE,COEFFICIENT)
		print(material)
	return 0 	
			



if __name__ == '__main__':
	interactive()		
					