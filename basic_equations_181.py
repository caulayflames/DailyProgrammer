# /r/Dailyprogrammer Challenge 181: Basic Equations
# http://redd.it/2h5b2k

"""Returns a and b for an equation"""
def parse_eq(equation):

	new_eqation = equation.lstrip(r'y=')	
	a,b = new_eqation.split('x')

	if a == '':
		a = 0
	if b == '':
		b = 0

	return float(a), float(b)

"""Finds and prints the intersection of two equations"""
def find_intersection(eq1, eq2):

	a1,b1 = parse_eq(eq1)
	a2,b2 = parse_eq(eq2)


	x = (b1 - b2)/(a2 - a1)
	y = (a2*b1 - a1*b2)/(a2-a1)


	if x.is_integer():
		x = int(x)
	if y.is_integer():
		y = int(y)

	print ('(%s,%s)' % (x, y))

find_intersection('2x+2','y=5x-4')
find_intersection('y=-5x','y=-4x+1')
find_intersection('y=0.5x+1.3','y=-1.4x-0.2')
