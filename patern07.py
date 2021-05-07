import driver
#pattern01
def letter(row,col):
	
	if (row >=3 and row <= 4) and (col >=5 and col <= 10):
		return "z"

	elif (row >= and row <=) and (col>=3 and col <= 6 ):
		return "X"

	elif (row >= and row <=) and (col>=3 and col <= 6 ):
		return "B"
	else: 
		return "S"

if __name__ == '__main__':
   driver.comparePatterns(letter)
