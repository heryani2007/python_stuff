from calculator import square

def test_square():
	assert square(2) == 4
	assert square(3) == 9

if __name__ == "__main__":
	test_square()
