import numpy as np
from astropy.table import Table

def sinPrint():
	x = np.linspace(0, 2*np.pi, 1000)
	y = np.linspace(np.sin(0), np.sin(2*np.pi), 1000)
	sinTable = Table([x, y],names=['x','sin(x)'])
	print(sinTable)

def main():
	sinPrint();


if __name__ == "__main__":
	main()