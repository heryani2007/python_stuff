'''
balance = 0

def main():
    print (f"Balance: {balance}")
    deposit (100)
    withdraw (50)
    print (f"Balance: {balance}")

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
'''
balance = 0

def main():
    global balance
    print (f"Balance: {balance}")
    balance = 20
    print (f"Balance: {balance}")

if __name__ == "__main__":
    main()
