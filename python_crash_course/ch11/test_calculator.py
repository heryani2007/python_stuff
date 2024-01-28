from calculator import square

def test_square():
	if square(2) != 4:
		print ("2 squared not 4 ")
	if square(3) != 9:
		print("3 squared not 9")
test_square()
