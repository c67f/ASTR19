def equation(x):
	xExp = x ** 3
	return xExp + 8

def main():
	result = equation(9)
	if result > 27:
		print("YAY!")

if __name__ == "__main__":
	main()