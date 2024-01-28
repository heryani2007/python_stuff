import pytest
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("Error")

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()
