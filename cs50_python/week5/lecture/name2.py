import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    for arg in sys.argv[1:3]:
        print(f"Hellow my name is {arg}")

main()
