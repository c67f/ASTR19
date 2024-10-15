
class Animal:

	def print(self):
		print("This animal has:")
		print(f"front limbs that are probably around {self.armLength} inches long")
		print(f"back limbs that are probably around {self.legLength} inches long")
		print(f"{self.eyes} eyes")
		if self.tail:
			print("does have a tail")
		else:
			print("does not have a tail")
		if self.furry:
			print("and is furry")
		else:
			print("and is not furry")

	def __init__(self):
		self.armLength =  float(1.5)
		self.legLength = float(2.0)
		self.eyes = int(2)
		self.tail = bool(1)
		self.furry = bool(0)


def main():
	giantIsopod = Animal()
	giantIsopod.print();

if __name__ == "__main__":
	main()