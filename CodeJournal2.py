def sum():
	a = 1.5
	b = 2.6
	c = a + b
	print(c) #4.1
	#print ()
	print("c's type is: " + str(type(c)))

def diff():
	a = 6.24
	b = 8.15
	c = a - b #0.91
	print(c)
	print("c's type is: " + str(type(c)))

def product():
	a = 7.1
	b = 2.0
	c = a * b
	#print(type(b))
	print(c)
	print("c's type is " + str(type(c)))

def main():
	sum()
	diff()
	product()

if __name__=="__main__":
	main()