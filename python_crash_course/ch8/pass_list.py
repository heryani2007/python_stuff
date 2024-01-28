def greet(userlist):
	for user in userlist:
		print (f"Hi {user}")

userlist = ["alice", "bob", "charlie"]

if __name__ == "__main__":
	greet(userlist)
