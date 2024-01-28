'''
def main():
    yell(["this", "is","cs50"])

def yell(words):
    for word in words:
        print(word.upper())

if __name__ == "__main__":
    main()
'''
def main():
    yell("this", "is","cs50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
