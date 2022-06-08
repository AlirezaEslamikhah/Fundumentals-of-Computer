quarter = 25
dim = 10 
nickel = 5
penny = 1 
def tedad(m):
	n = 100 - m
	x = n % quarter
    if x == 0 : 
		print (n// quarter + quarter)
	# elif n % nickel == 0:
	# 	print (n// quarter + quarter +  )


tedad(0)